from odoo import http
from odoo.http import request

class BikeRentalController(http.Controller):
    @http.route('/bikes', auth='public', website=True)
    def bike_list(self, **kwargs):
        bikes = request.env['bike.rental'].sudo().search([('is_available', '=', True)])
        return request.render('bike_rental.bike_list_template', {'bikes': bikes})

    @http.route('/bikes/request', auth='public', website=True, methods=['POST'])
    def bike_request(self, **post):
        name = post.get('name')
        bike_id = post.get('bike_id')
        duration = post.get('duration')
        if name and bike_id and duration:
            try:
                duration = int(duration)
                request.env['bike.rental.request'].sudo().create({
                    'name': name,
                    'bike_id': int(bike_id),
                    'duration': duration,
                })
                return request.render('bike_rental.bike_request_success_template', {})
            except Exception as e:
                return request.render('bike_rental.bike_request_error_template', {'error': str(e)})
        return request.render('bike_rental.bike_request_error_template', {'error': 'Missing required fields'})