from odoo import http
from odoo.http import request
from datetime import datetime

class BikeRentalController(http.Controller):

    @http.route('/bikes', type='http', auth='public', website=True)
    def bike_list(self, **kwargs):
        """Display list of available bikes"""
        bikes = request.env['bike.rental'].sudo().search([('is_available', '=', True)])
        
        values = {
            'bikes': bikes,
            'success': kwargs.get('success'),
            'error': kwargs.get('error'),
        }
        return request.render('bike_rental.bike_list_template', values)

    @http.route('/bikes/request', type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def bike_request(self, **post):
        """Handle bike rental request submission"""
        try:
            # Validate input
            bike_id = int(post.get('bike_id'))
            name = post.get('name')
            start_date = post.get('start_date')
            duration = int(post.get('duration'))
            
            if not all([bike_id, name, start_date, duration]):
                return request.redirect('/bikes?error=Missing required fields')
            
            # Validate start date
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
            if start_date_obj < datetime.now().date():
                return request.redirect('/bikes?error=Start date cannot be in the past')
            
            # Validate duration
            if duration < 1:
                return request.redirect('/bikes?error=Duration must be at least 1 day')
            
            # Check if bike exists and is available
            bike = request.env['bike.rental'].sudo().browse(bike_id)
            if not bike.exists() or not bike.is_available:
                return request.redirect('/bikes?error=Selected bike is not available')
            
            # Create rental request
            request.env['bike.rental.request'].sudo().create({
                'name': name,
                'bike_id': bike_id,
                'start_date': start_date,
                'duration': duration,
                'user_id': request.env.user.id if not request.env.user._is_public() else False,
            })
            
            return request.redirect('/bikes?success=Rental request submitted successfully!')
            
        except Exception as e:
            return request.redirect('/bikes?error=Error submitting request. Please try again.')

    @http.route('/my/bike-requests', type='http', auth='user', website=True)
    def my_requests(self, **kwargs):
        """Display user's bike rental requests"""
        requests = request.env['bike.rental.request'].search([
            ('user_id', '=', request.env.user.id)
        ], order='request_date desc')
        
        values = {
            'requests': requests,
        }
        return request.render('bike_rental.my_requests_template', values)
