# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    app_saas_ok = fields.Boolean('Enable CN SaaS', default=True, config_parameter='app_saas_ok',
                                 help="Checked to Enable www.odooapp.cn cloud service.")
    app_saas_db_token = fields.Char('SaaS DB Token', config_parameter='app_saas_db_token')

    def set_values(self):
        res = super().set_values()
        self.env['ir.config_parameter'].set_param('app_saas_db_token', self.app_saas_db_token)
        return res
