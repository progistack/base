# -*- coding: utf-8 -*-
{
    'name': "Ruban d'environnement",

    'summary': """
        Ruban d'alert de l'environnement""",

    'description': """
        Le ruban d'environnement est une alerte indiquant à l'utilisateur l'environnement sur lequel celui-ci se trouve.
    """,

    "sequence": "-200",
    'version': '0.1',
    'author': "ELYDEV",
    'website': "https://www.progistack.com",
    'category': 'Extra Tools',

    'depends': [
        'base_setup',
    ],

    'data': [
        'views/menu.xml',
        'data/ir_config_parameter_data.xml',
        'views/app_theme_config_settings_views.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'env_ribbon/static/src/scss/ribbon.scss',
            'env_ribbon/static/src/js/ribbon.js',
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
}
