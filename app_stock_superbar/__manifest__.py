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
    'name': 'Stock Superbar - Location Tree Navigation',
    'version': '18.0.24.12.03',
    'author': 'TrixocomERP',
    'category': 'Inventory/Inventory',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '''
    Use for parent-children tree list select navigator. Stock location tree, filter by parent location.
    ztree widget. Inventory multi-level tree navigation application.
    ''',
    'description': '''
    Stock Superbar - Inventory Multi-Level Tree Navigation
    
    Navigate stock locations with hierarchical tree structure.
    Filter by parent location for easy inventory management.
    
    Features:
    - Location hierarchy navigation
    - Parent-children tree selector
    - ztree widget integration
    - Multi-level tree navigation for inventory
    ''',
    'depends': [
        'stock',
        'app_stock_ztree',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/stock_location_views.xml',
        'views/stock_picking_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
