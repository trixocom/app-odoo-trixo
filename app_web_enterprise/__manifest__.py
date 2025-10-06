# -*- coding: utf-8 -*-

# Created on 2018-12-01
# author: TrixocomERP, https://www.trixocom.com
# email: info@trixocom.com
# Copyright (C) 2009~2024 TrixocomERP

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
    'name': 'Web Enterprise UI Enhancement',
    'version': '18.0.24.12.03',
    'author': 'TrixocomERP',
    'category': 'Hidden',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '''
    Odoo Enterprise version UI enhancement.
    1. Add dropdown arrow to parent menu.
    2. Replace the odoo logo to your company logo in main menu.
    3. Always show search in main menu.
    ''',
    'description': '''
    Web Enterprise UI Enhancement
    
    TrixocomERP (trixocom.com) odoo module. Enterprise version interface enhancement.
    
    Features:
    1. Dropdown arrows appear in multi-level menus.
    2. Replace the logo in the main menu interface with your company's logo.
    3. Make search visible in the main menu interface.
    
    Enhance your Odoo Enterprise interface with improved navigation and branding.
    ''',
    'depends': [
        'web_enterprise',
    ],
    'images': ['static/description/banner.png'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'app_web_enterprise/static/src/**/*',
        ],
    },
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
