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
    'name': "MRP BOM Product Multi Batch Add",
    'version': '18.0.24.12.03',
    'author': 'TrixocomERP',
    'category': 'Manufacturing/Manufacturing',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    MRP BOM Product Multi Batch Add.
    Manufacturing BOM batch add products.
    """,
    'description': """
    App MRP BOM Product Multi Batch Add
    
    Add multiple products to Bill of Materials with one click.
    Filter and group products before adding.
    
    Manufacturing BOM batch add products:
    - Quick multi-product addition
    - Product filtering and grouping
    - Batch operations for BOM
    """,
    'depends': [
        'mrp',
    ],
    'images': ['static/description/banner.gif'],
    'data': [
        'views/mrp_bom_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
