
from odoo import fields,models,api,_

class ApplicantAttachmnet(models.TransientModel):
    _inherit = 'candidate.attachement'

    def action_confirm(self):
        applicant = self.env['hr.applicant'].browse(self.env.context.get('active_id'))
        print(applicant)

