{
    "name": "Bike Rental",
    "version": "1.0",
    "category": "Rental",
    "summary": "A simple bike rental module for Odoo with website integration.",
    "description": "This module allows users to rent bikes, manage rental records, track availability, and view bikes on a public website.",
    "author": "Kamal",
    "website": "https://yourwebsite.com",
    "depends": ["base", "website"],
    "data": [
        "security/ir.model.access.csv",
        "views/bike_rental_views.xml",
        "views/bike_rental_request_views.xml",
        "views/website_bike_rental_templates.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}