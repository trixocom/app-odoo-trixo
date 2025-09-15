# -*- coding: utf-8 -*-

# Created on 2023-02-02
# author: Trixocom, https://www.trixocom.com
# email: 300883@qq.com
# resource of trixocom
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Online user and developer manuals (long term updates)
# https://www.trixocom.com/documentation/16.0/en/index.html
# https://www.trixocom.com/documentation/16.0/en/developer.html

##############################################################################
#    Copyright (C) 2009-TODAY trixocom.com Ltd. https://www.trixocom.com
#    Author: Ivan Deng, 300883@qq.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
##############################################################################

{
    'name': "Trixocom Common Util and Tools, Trixocom core features and dashboard",
    'version': '16.0.25.03.10',
    'author': 'Trixocom',
    'category': 'Extra tools',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
    'summary': '''
    Core for common use for Trixocom apps.
    Core utilities and cloud dashboard, provides common fields and views for other modules.
    ''',
    'description': '''
    need to setup odoo.conf, add follow:
    server_wide_modules = web,app_common
    1. Quick import data from excel with .py code
    2. Quick m2o default value
    3. Filter for useless field
    4. UTC local timezone convert
    5. Get browser ua, user-agent
    6. Image to local, image url to local, media to local attachment
    7. Log cron job
    8. Boost for less no use mail
    9. Customize .rng file
    10. Misc like get distance between two points
    11. Multi-language Support. Multi-Company Support.
    12. Support Odoo 18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    13. Full Open Source.
    ''',
    'depends': [
        'mail',
        'base_setup',
        'web',
    ],
    'data': [
        'views/res_config_settings_views.xml',
        'views/ir_cron_views.xml',
        # 'report/.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
}
