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
    'name': 'Product Superbar - Category Tree Navigation',
    'version': '18.0.24.12.03',
    'author': 'TrixocomERP',
    'category': 'Sales/Sales',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '''
    Browse Product by category tree. Use for parent-children tree list kanban navigator.
    Easy to navigate and browse any data. Support list, kanban, pivot, graph view.
    ztree widget. Hierarchy Tree. Parent-Children relation tree.
    Product management multi-level tree navigation application.
    ''',
    'description': '''
    Product Superbar - Product Management Multi-Level Tree Navigation
    
    Browse products by category tree hierarchy.
    Easy to navigate and browse product data.
    
    Features:
    - Category hierarchy navigation
    - Support list, kanban, pivot, graph views
    - ztree widget integration
    - Parent-Children relation tree
    - Product management multi-level navigation
    ''',
    'depends': [
        'product',
        'app_product_ztree',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/product_template_views.xml',
        'views/product_product_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
