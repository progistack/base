# -*- coding: utf-8 -*-
{
    'name': "Ruban d'environnement",
    'summary': """Ruban d'alert de l'environnement""",
    'description': """
        Le ruban d'environnement est une alerte indiquant à l'utilisateur l'environnement sur lequel celui-ci se trouve.
    """,
    'author': "ELYDEV",
    'maintainer': 'ELYDEV',
    "support": "elydev01@gmail.com",
    'website': "https://www.github.com/elydev01/",
    'category': 'Extra Tools',
    'version': '0.1',
    "sequence": "-200",
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
    'images': ['static/description/icon.png'],
    "license": "AGPL-3",
    'installable': True,
    'application': True,
    'auto_install': False,
}
