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
    'name': 'MRP Superbar - Manufacturing Tree Navigation',
    'version': '18.0.24.12.03',
    'author': 'TrixocomERP',
    'category': 'Manufacturing/Manufacturing',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '''
    MRP Manufacturing multi-level tree navigation.
    ztree widget. Hierarchy Tree navigation for manufacturing orders.
    ''',
    'description': '''
    MRP Superbar - Manufacturing Multi-Level Tree Navigation
    
    Navigate manufacturing orders with hierarchical tree structure.
    Easy access to production data.
    
    Features:
    - Manufacturing order hierarchy
    - ztree widget integration
    - Multi-level tree navigation for MRP
    ''',
    'depends': [
        'mrp',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/mrp_production_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
