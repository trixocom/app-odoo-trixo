# -*- coding: utf-8 -*-

# Created on 2023-02-02
# author: TrixocomERP, https://www.trixocom.com
# email: info@trixocom.com
# resource of TrixocomERP
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo Online Chinese User Manual (Long-term updates)
# https://www.trixocom.com/documentation/user/

# Odoo Offline Chinese User Manual Download
# https://www.trixocom.com/odoo_user_manual_document_offline/

# Odoo Offline Development Manual Download - includes Python tutorial, jQuery reference, Jinja2 templates, PostgreSQL reference (essential for Odoo development)
# https://www.trixocom.com/odoo_developer_document_offline/

{
    'name': 'Odoo Chinese Localization Suite - Chinese Accounting Foundation, All in One Enhancement',
    'version': '18.0.25.09.29',
    'author': 'TrixocomERP',
    'category': 'Base',
    'website': 'https://www.trixocom.com',
    'live_test_url': 'https://demo.trixocom.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0,
    'currency': 'EUR',
    'summary': '''
    Odoo Simplified Chinese Version Comprehensive Enhancement. More politically sensitive translations. Chinese enhance. Out of the box use odoo in China. Chinese address format, number format, money format.
    Set all chinese default values. Default country, timezone, currency, partner. Chinese accounting foundation module.
    ''',
    'description': '''
    Odoo Chinese Enhancement - Foundation
    
    Features:
    1. Chinese address format, applicable to all Chinese customers, suppliers, partners, users, employee information etc.
    2. Chinese default values such as country/region, time zone, currency, etc. Handles base and product modules.
    3. Add customer abbreviation, Chinese address display, customer code display priority
    4. Customer address display adds mobile and phone numbers
    5. Currency processing, RMB enhancement, add sorting display
    6. Fixed bug where category list and m2o field don't display Chinese directory names
    7. Fixed bug where warehouse location list and m2o field don't display Chinese directory names
    8. Super user changed timezone to China
    9. Date format is year-month-day (e.g., 2023-08-08) and time is 12:34 (China format)
    10. Country/region sorting added; China ranked first
    11. Display payment-related information according to Chinese habits
    12. Translation export defaults to Chinese, default po format
    13. [Default removed, can be loaded via .py] Add name_en_US field in base model, updates translation value when assigned
    14. Common decimal precision adjustments
    15. Sales team changed to China
    16. Simplified language display, e.g. Chinese Simplified to Chinese
    17. Process 'Country' field as 'Country/Region' to avoid policy sensitivity issues (works with TrixocomERP Chinese translation)
    
    Additional Features:
    21. Multi-language Support
    22. Multi-Company Support
    23. Support Odoo 18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition
    24. Full Open Source
    ''',
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'depends': [
        'base_address_extended',
        'resource',
        'account',
        'sales_team',
        'sale',
        'delivery',
        'stock',
        'app_odoo_customize',
    ],
    'images': ['static/description/banner.jpg'],
    'data': [
        'views/res_partner_views.xml',
        'views/res_currency_views.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'views/ir_default_views.xml',
        'views/ir_module_module_views.xml',
        # 'views/templates.xml',
        'wizard/sale_make_invoice_advance_views.xml',
        'data/base_data.xml',
        'data/uom_uom_data.xml',
        'data/decimal_precision_data.xml',
        'data/res_country_data.xml',
        'data/res_currency_data.xml',
        'data/res_lang_data.xml',
        'data/res_company_data.xml',
        'data/res_partner_data.xml',
        'data/res_users_data.xml',
        'data/resource_calendar_data.xml',
        'data/product_category_data.xml',
        'data/product_pricelist_data.xml',
        'data/stock_location_data.xml',
        'data/stock_picking_type_data.xml',
        'data/sales_team_data.xml',
        'data/ir_default_data.xml',
        'data/ir_config_parameter_data.xml',
        'data/spreadsheet_dashboard_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'app_base_chinese/static/src/scss/app_style.scss',
        ]
    },
    'demo': [
        'demo/res_company_demo.xml',
        'demo/res_partner_demo.xml',
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
