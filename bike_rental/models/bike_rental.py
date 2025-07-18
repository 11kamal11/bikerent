from odoo import models, fields

class BikeRental(models.Model):
    _name = 'bike.rental'
    _description = 'Bike Rental Management'

    name = fields.Char(string='Bike Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Rental Price', required=True)
    rental_duration = fields.Integer(string='Rental Duration (days)', required=True)
    is_available = fields.Boolean(string='Available', default=True)
    image = fields.Binary(string='Image', attachment=True)