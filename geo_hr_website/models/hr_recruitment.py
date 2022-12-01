from odoo import fields,models,api,_


class HrJob(models.Model):
    _inherit = 'hr.job'

    def set_publish(self):
        self.is_published = True

    def set_unpublish(self):
        self.is_published = False