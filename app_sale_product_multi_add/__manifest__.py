# -*- coding: utf-8 -*-

# Created on 2023-10-20
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
    'name': "Sale Order Product Multi Batch Add",
    'version': '18.0.24.12.03',
    'author': 'TrixocomERP',
    'category': 'Sales/Sales',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Sale Order Product Multi Batch Add.
    One Click to add multiple products to Sale Order.
    All the products can filter and group.
    """,
    'description': """
    Sale Order Product Multi Add
    
    1. One Click to add multiple products to Sale Order.
    2. All the products can filter and group.
    
    Sales order batch add products:
    1. Can quickly add multiple products to sales order with one click
    2. Can filter and group products, then add in batches
    """,
    'depends': [
        'sale',
    ],
    'images': ['static/description/banner.gif'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
