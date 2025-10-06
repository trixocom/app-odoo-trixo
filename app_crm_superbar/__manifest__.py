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
    'name': 'CRM Superbar - Pipeline Tree Navigation',
    'version': '18.0.24.12.03',
    'author': 'TrixocomERP',
    'category': 'Sales/CRM',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '''
    CRM multi-level tree navigation.
    Browse CRM leads and opportunities with hierarchy tree.
    ztree widget integration.
    ''',
    'description': '''
    CRM Superbar - CRM Multi-Level Tree Navigation
    
    Navigate CRM leads and opportunities with hierarchical tree structure.
    Easy access to sales pipeline data.
    
    Features:
    - CRM pipeline hierarchy
    - ztree widget integration
    - Multi-level tree navigation for CRM
    ''',
    'depends': [
        'crm',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
