# -*- coding: utf-8 -*-

# Created on 2023-02-02
# author: TrixocomERP, https://www.trixocom.com
# email: info@trixocom.com
# resource of TrixocomERP
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo Online User Manual (Long-term updates)
# https://www.trixocom.com/documentation/user/

# Odoo Online Developer Manual (Long-term updates)
# https://www.trixocom.com/documentation/developer/

##############################################################################
#    Copyright (C) 2009-TODAY TrixocomERP Ltd. https://www.trixocom.com
#    Author: TrixocomERP Team, info@trixocom.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
##############################################################################

{
    'name': "TrixocomERP Common Util and Tools - Base Functions and Panel",
    'version': '18.0.25.09.12',
    'author': 'TrixocomERP',
    'category': 'Extra tools',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
    'summary': '''
    Core for common use for TrixocomERP apps.
    Base core and cloud panel, must have no dependent fields and views to implement auto_install
    ''',
    'description': '''
    need to setup odoo.conf, add follow:
    server_wide_modules = web,app_common
    
    Features:
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
    11. Multi-language Support
    12. Multi-Company Support
    13. Support Odoo 18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition
    14. Full Open Source
    ''',
    'depends': [
        'mail',
        'base_setup',
        'web',
    ],
    'data': [
        'data/ir_module_category_data.xml',
        'wizard/mail_compose_message_views.xml',
        'views/res_config_settings_views.xml',
        'views/ir_cron_views.xml',
        # 'report/.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [],
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
    # 'external_dependencies': {'python': ['pyyaml', 'ua-parser', 'user-agents']},
    'installable': True,
    'application': True,
    'auto_install': True,
}
