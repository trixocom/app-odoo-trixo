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
    'name': 'Company Organization Chart - Tree Navigation',
    'version': '18.0.24.12.03',
    'author': 'TrixocomERP',
    'category': 'Base',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '''
    Company organization chart with tree structure.
    Browse companies by hierarchy tree.
    Multi-level company navigation.
    ''',
    'description': '''
    Company Organization Chart - Tree Navigation
    
    Browse companies using hierarchical tree structure.
    Easy navigation through company organization.
    
    Features:
    - Company hierarchy tree
    - Organization chart view
    - Multi-level navigation
    - Parent-child company relationships
    ''',
    'depends': [
        'base',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/res_company_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
