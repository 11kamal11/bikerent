{
    "name": "Bike Rental",
    "version": "1.0",
    "category": "Rental",
    "summary": "A simple bike rental module for Odoo.",
    "description": "This module allows users to rent bikes, manage rental records, and track availability.",
    "author": "Kamal",
    "website": "https://yourwebsite.com",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/bike_rental_views.xml"
    ],
    "installable": true,
    "application": true,
    "auto_install": false
}