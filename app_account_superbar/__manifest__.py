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
    'name': 'Account Superbar - Multi-Level Tree Navigation',
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
    Browse journal by account chart. Use for parent-children tree list kanban navigator.
    ztree widget. Hierarchy Tree. Parent-Children relation tree.
    Financial module multi-level tree navigation application.
    ''',
    'description': '''
    Account Superbar - Financial Module Multi-Level Tree Navigation
    
    Browse journal entries by account chart hierarchy.
    Use for parent-children tree list kanban navigator.
    
    Features:
    - ztree widget integration
    - Hierarchy Tree navigation
    - Parent-Children relation tree
    - Financial module multi-level tree navigation
    - Easy navigation through account structures
    ''',
    'depends': [
        'account',
        'app_account_ztree',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/account_account_views.xml',
        'views/account_move_views.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
