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
    'name': 'Account Ztree - Tree Selector Widget',
    'version': '18.0.24.12.03',
    'author': 'TrixocomERP',
    'category': 'Accounting/Accounting',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'EUR',
    'summary': '''
    Use for parent-children tree list select navigator. Multi Level Account Chart tree. ztree widget.
    Financial module tree selector.
    ''',
    'description': '''
    Account Ztree - Financial Module Tree Selector
    
    Use for parent-children tree list select navigator.
    Multi Level Account Chart tree with ztree widget.
    
    Features:
    - Tree selector for account charts
    - Multi-level navigation
    - Parent-children relationship display
    - Easy account selection
    - ztree widget integration
    ''',
    'depends': [
        'account',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/account_account_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'app_account_ztree/static/src/**/*',
        ],
    },
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
