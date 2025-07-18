from odoo import http
from odoo.http import request
import json
from datetime import datetime

class BikeRentalController(http.Controller):
    @http.route('/bikes', auth='public', website=True)
    def bike_list(self, **kwargs):
        price_filter = float(kwargs.get('price_filter', 0)) if kwargs.get('price_filter') else None
        domain = [('is_available', '=', True)]
        if price_filter:
            domain.append(('price', '<=', price_filter))
        bikes = request.env['bike.rental'].sudo().search(domain)
        return request.render('bike_rental.bike_list_template', {
            'bikes': bikes,
            'price_filter': price_filter or '',
        })

    @http.route('/bikes/request', auth='public', website=True, methods=['POST'])
    def bike_request(self, **post):
        name = post.get('name')
        bike_id = post.get('bike_id')
        start_date = post.get('start_date')
        duration = post.get('duration')
        if name and bike_id and start_date and duration:
            try:
                duration = int(duration)
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                request.env['bike.rental.request'].sudo().create({
                    'name': name,
                    'bike_id': int(bike_id),
                    'start_date': start_date,
                    'duration': duration,
                })
                return request.render('bike_rental.bike_request_success_template', {})
            except Exception as e:
                return request.render('bike_rental.bike_request_error_template', {'error': str(e)})
        return request.render('bike_rental.bike_request_error_template', {'error': 'Missing required fields'})

    @http.route('/my/bike-requests', auth='user', website=True)
    def my_requests(self, **kwargs):
        requests = request.env['bike.rental.request'].sudo().search([('user_id', '=', request.env.user.id)])
        return request.render('bike_rental.my_requests_template', {'requests': requests})

    @http.route('/bikes/availability', auth='public', website=True)
    def bike_availability(self, **kwargs):
        bikes = request.env['bike.rental'].sudo().search([('is_available', '=', True)])
        events = []
        for bike in bikes:
            # Simulate availability events (in a real scenario, check rental periods)
            events.append({
                'title': bike.name,
                'start': datetime.now().strftime('%Y-%m-%d'),
                'end': datetime.now().strftime('%Y-%m-%d'),
            })
        return json.dumps(events)