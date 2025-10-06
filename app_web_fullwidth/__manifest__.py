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
    'name': 'Form View Responsive Full Width',
    'version': '18.0.24.12.03',
    'author': 'TrixocomERP',
    'category': 'Hidden',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '''
    Form view Responsive full width (fullwidth).
    Ready for small, medium, large, extra large screen.
    Ready for enterprise and community version.
    ''',
    'description': '''
    Form View Responsive Full Width
    
    Form view responsive full width display.
    Ready for all screen sizes: small, medium, large, extra large.
    Compatible with both enterprise and community versions.
    
    Features:
    - Full screen form display
    - Responsive design
    - Multi-screen size support
    - Enterprise and Community compatible
    ''',
    'depends': [
        'web',
    ],
    'images': ['static/description/banner.png'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'app_web_fullwidth/static/src/**/*',
        ],
    },
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
