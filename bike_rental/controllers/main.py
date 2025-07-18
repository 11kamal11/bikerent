from odoo import http
from odoo.http import request
import logging
from datetime import datetime

_logger = logging.getLogger(__name__)

class BikeRentalController(http.Controller):
    @http.route('/', auth='public', website=True, type='http', website=False, priority=1)
    def home(self, **kwargs):
        _logger.info("Accessed custom home route with kwargs: %s", kwargs)
        price_filter = float(kwargs.get('price_filter', 0)) if kwargs.get('price_filter') else None
        domain = [('is_available', '=', True)]
        if price_filter:
            domain.append(('price', '<=', price_filter))
        bikes = request.env['bike.rental'].sudo().search(domain)
        _logger.info("Rendering home with %d bikes, price_filter=%s", len(bikes), price_filter)
        if not bikes:
            _logger.warning("No bikes found for domain: %s", domain)
        response = request.render('bike_rental.bike_list_template', {
            'bikes': bikes,
            'price_filter': price_filter or '',
        })
        if not response:
            _logger.error("Failed to render bike_list_template, returning fallback")
            return "<h1>Bike Rental Page (Fallback)</h1><p>Check logs for details.</p>"
        return response

    @http.route('/bikes', auth='public', website=True, type='http')
    def bike_list(self, **kwargs):
        _logger.info("Accessed /bikes route with kwargs: %s", kwargs)
        price_filter = float(kwargs.get('price_filter', 0)) if kwargs.get('price_filter') else None
        domain = [('is_available', '=', True)]
        if price_filter:
            domain.append(('price', '<=', price_filter))
        bikes = request.env['bike.rental'].sudo().search(domain)
        _logger.info("Rendering bike list with %d bikes, price_filter=%s", len(bikes), price_filter)
        if not bikes:
            _logger.warning("No bikes found for domain: %s", domain)
        response = request.render('bike_rental.bike_list_template', {
            'bikes': bikes,
            'price_filter': price_filter or '',
        })
        if not response:
            _logger.error("Failed to render bike_list_template, returning fallback")
            return "<h1>Bike Rental Page (Fallback)</h1><p>Check logs for details.</p>"
        return response

    @http.route('/bikes/request', auth='public', website=True, methods=['POST'], type='http')
    def bike_request(self, **post):
        _logger.info("Received /bikes/request with post data: %s", post)
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
                _logger.info("Rental request created successfully for bike_id=%s", bike_id)
                return request.render('bike_rental.bike_request_success_template', {})
            except Exception as e:
                _logger.error("Error processing request: %s", str(e))
                return request.render('bike_rental.bike_request_error_template', {'error': str(e)})
        return request.render('bike_rental.bike_request_error_template', {'error': 'Missing required fields'})

    @http.route('/my/bike-requests', auth='user', website=True, type='http')
    def my_requests(self, **kwargs):
        _logger.info("Accessed /my/bike-requests for user: %s", request.env.user.name)
        requests = request.env['bike.rental.request'].sudo().search([('user_id', '=', request.env.user.id)])
        _logger.info("Rendering my requests with %d requests", len(requests))
        return request.render('bike_rental.my_requests_template', {'requests': requests})