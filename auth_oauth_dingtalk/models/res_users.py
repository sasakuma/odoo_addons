# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import except_orm, Warning, RedirectWarning,AccessDenied
import odoo.addons.decimal_precision as dp

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def auth_oauth_dingtalk(self,provide_id,userid):
        user_ids=self.search([('oauth_provider_id','=',provide_id),('oauth_uid','=',userid)])
        if not user_ids or len(user_ids)>1:
            return AccessDenied
        return (self.env.cr.dbname, user_ids[0].login, userid)

    @api.model
    def check_credentials(self, password):
        try:
            return super(ResUsers, self).check_credentials(password)
        except AccessDenied:
            res = self.sudo().search([('id', '=', self.env.uid), ('oauth_uid', '=', password)])
            if not res:
                raise


    

