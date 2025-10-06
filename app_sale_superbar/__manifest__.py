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
    'name': 'Sales Superbar - Multi-Level Navigation',
    'version': '18.0.24.12.03',
    'author': 'TrixocomERP',
    'category': 'Sales/Sales',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '''
    Browse sale order by partner and sale channel. Use for parent-children tree list kanban navigator.
    ztree widget. Hierarchy Tree. Parent-Children relation tree.
    Sales multi-level tree navigation application.
    ''',
    'description': '''
    Sales Superbar - Sales Multi-Level Tree Navigation
    
    Browse sale orders by partner and sales channel.
    Easy navigation through sales data.
    
    Features:
    - Partner hierarchy navigation
    - Sales channel organization
    - ztree widget integration
    - Parent-Children relation tree
    - Multi-level tree navigation for sales
    ''',
    'depends': [
        'sale',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
