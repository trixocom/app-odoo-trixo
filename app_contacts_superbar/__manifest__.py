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
    'name': 'Contacts Superbar - Multi-Level Tree Navigation',
    'version': '18.0.24.12.03',
    'author': 'TrixocomERP',
    'category': 'Sales/CRM',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '''
    Browse contacts by company. Use for parent-children tree list kanban navigator.
    ztree widget. Hierarchy Tree. Parent-Children relation tree.
    Contacts module multi-level tree navigation application.
    ''',
    'description': '''
    Contacts Superbar - Multi-Level Tree Navigation
    
    Browse contacts by company hierarchy.
    Easy navigation through contact structures.
    
    Features:
    - ztree widget integration
    - Hierarchy Tree navigation
    - Parent-Children relation tree
    - Multi-level tree navigation for contacts
    ''',
    'depends': [
        'contacts',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
