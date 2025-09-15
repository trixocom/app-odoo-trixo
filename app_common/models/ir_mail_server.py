# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class IrMailServer(models.Model):
    _inherit = "ir.mail_server"
    _order = "sequence"
    
    # Change default email sending logic
    @api.model
    def send_email(self, message, mail_server_id=None, smtp_server=None, smtp_port=None,
                   smtp_user=None, smtp_password=None, smtp_encryption=None, smtp_debug=False,
                   smtp_session=None):

        email_to = message['To']
        
        # Ignore invalid emails to avoid being banned
        if email_to:
            if email_to.find('no-reply@trixocom.com') != -1 or email_to.find('postmaster-odoo@trixocom.com') != -1:
                pass
            elif email_to.find('example.com') != -1 or email_to.find('@sunpop.cn') != -1 or email_to.find('@odooapp.cn') != -1:
                _logger.warning(_("=================Email to ignore: %s") % email_to)
                raise AssertionError(_("Email to ignore: %s") % email_to)

        return super(IrMailServer, self).send_email(message, mail_server_id, smtp_server, smtp_port,
                                                    smtp_user, smtp_password, smtp_encryption, smtp_debug,
                                                    smtp_session)
