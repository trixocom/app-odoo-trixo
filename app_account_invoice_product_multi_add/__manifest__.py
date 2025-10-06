# -*- coding: utf-8 -*-

# Created on 2023-10-20
# author: TrixocomERP, https://www.trixocom.com
# email: info@trixocom.com
# Copyright (C) 2009~2024 TrixocomERP

# Odoo Online User Manual (Long-term updates)
# https://www.trixocom.com/documentation/user/

# Odoo Online Developer Manual (Long-term updates)
# https://www.trixocom.com/documentation/developer/

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
    'name': "App Account Invoice Product Multi Batch Add",
    'version': '18.0.24.12.03',
    'author': 'TrixocomERP',
    'category': 'Accounting/Accounting',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'USD',
    'summary': """
    App Account Invoice Product Multi Batch Add
    TrixocomERP Odoo App
    """,
    'description': """
    App Account Invoice Product Multi Add
    1. One Click to add multiple products to Account Invoice.
    2. All the products can filter and group.
    
    Customer Receipt and Supplier Bill Batch Add Products
    1. Can quickly add multiple products to customer receipts and supplier bills with one click
    2. Can filter and group products, then add in batches
    """,
    'depends': [
        # 'app_web_one2many_multi_add',
        'account',
    ],
    'images': ['static/description/account1.gif'],
    'data': [
        'views/account_move_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}
