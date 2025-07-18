{
    "name": "Bike Rental",
    "version": "1.0",
    "category": "Rental",
    "summary": "A simple bike rental module for Odoo with enhanced website integration.",
    "description": "This module allows users to rent bikes, manage rental records, track availability, and interact via a public website with advanced features.",
    "author": "Kamal",
    "website": "https://11kamal11-bikerent.odoo.com/",
    "depends": ["base", "website", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/bike_rental_views.xml",
        "views/bike_rental_request_views.xml",
        "views/website_bike_rental_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "bike_rental/static/src/css/bike_rental.css",
            "bike_rental/static/src/js/bike_rental.js",
            "https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/5.11.0/main.min.css",
            "https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/5.11.0/main.min.js",
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
}