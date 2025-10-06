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
    'name': 'HR Superbar - Employee Department Tree Navigation',
    'version': '18.0.24.12.03',
    'author': 'TrixocomERP',
    'category': 'Human Resources/Employees',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '''
    Browse employees by departments tree. HR organization chart.
    Easy to navigate and browse any data. Support list, kanban, pivot, graph view.
    ztree widget. HR Hierarchy organization chart Tree.
    Human Resources module multi-level tree navigation application.
    ''',
    'description': '''
    HR Superbar - Human Resources Multi-Level Tree Navigation
    
    Browse employees by departments tree with HR organization chart.
    Easy to navigate and browse any data.
    
    Features:
    - Department hierarchy navigation
    - Support list, kanban, pivot, graph views
    - ztree widget integration
    - HR organization chart tree
    - View employees by department
    - Super convenient queries
    ''',
    'depends': [
        'hr',
        'app_hr_ztree',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/hr_employee_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
