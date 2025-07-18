from odoo import models, fields

class BikeRental(models.Model):
    _name = 'bike.rental'
    _description = 'Bike Rental Management'

    name = fields.Char(string='Bike Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Rental Price', required=True)
    rental_duration = fields.Integer(string='Rental Duration (days)', required=True)
    is_available = fields.Boolean(string='Available', default=True)

    def rent_bike(self):
        self.is_available = False

    def return_bike(self):
        self.is_available = True

    def update_rental_price(self, new_price):
        self.price = new_price

    def get_bike_info(self):
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'is_available': self.is_available,
        }