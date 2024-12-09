# -*- coding: utf-8 -*-
{
    "name": "Custom Event",
    "summary": "Event Management",
    "description": """
        Custom Event Management
    """,
    "author": "Mohiuddin",
    "website": "mohiuddinru.github.io",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["base", "web", "website"],
    "data": [
        'security/ir.model.access.csv',
        "views/snippet_template.xml",
        "views/views.xml",
        "views/templates.xml",
    ],
    "assets": {
        'web.assets_frontend': [
            "/custom_event/static/src/components/**/*"
        ],
    }
}

