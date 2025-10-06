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
    'name': 'Event Superbar - Multi-Level Navigation',
    'version': '18.0.24.12.03',
    'author': 'TrixocomERP',
    'category': 'Marketing/Events',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '''
    Event module multi-level tree navigation.
    Browse events with hierarchy structure.
    ztree widget integration.
    ''',
    'description': '''
    Event Superbar - Event Multi-Level Tree Navigation
    
    Navigate events with hierarchical tree structure.
    Easy access to event data.
    
    Features:
    - Event hierarchy navigation
    - ztree widget integration
    - Multi-level tree navigation for events
    ''',
    'depends': [
        'event',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/event_event_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
