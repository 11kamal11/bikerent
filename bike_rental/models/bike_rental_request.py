from odoo import models, fields

class BikeRentalRequest(models.Model):
    _name = 'bike.rental.request'
    _description = 'Bike Rental Request'

    name = fields.Char(string='Customer Name', required=True)
    bike_id = fields.Many2one('bike.rental', string='Bike', required=True)
    request_date = fields.Date(string='Request Date', default=fields.Date.today)
    start_date = fields.Date(string='Start Date', required=True)
    duration = fields.Integer(string='Requested Duration (days)', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft')
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user)