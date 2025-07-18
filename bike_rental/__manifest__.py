{
    "name": "Bike Rental",
    "version": "1.0",
    "category": "Rental",
    "summary": "A simple bike rental module for Odoo with enhanced website integration.",
    "description": "This module allows users to rent bikes, manage rental records, track availability, and interact via a custom public website.",
    "author": "Kamal",
    "website": "https://yourwebsite.com",
    "depends": ["base", "website", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/bike_rental_views.xml",
        "views/bike_rental_request_views.xml",
        "views/website_bike_rental_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "bike_rental/static/src/css/bike_rental.css?v=1.1",
            "bike_rental/static/src/js/bike_rental.js?v=1.1",
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
}