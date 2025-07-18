{
    "name": "Bike Rental",
    "version": "1.0",
    "category": "Rental",
    "summary": "A simple bike rental module for Odoo.",
    "description": "This module allows users to rent bikes, manage rental records, and track availability.",
    "author": "Kamal",
    "website": "https://youtube.com",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/bike_rental_views.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}