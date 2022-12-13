from odoo import fields,models,api,_


class HrJob(models.Model):
    _inherit = 'hr.job'

    def set_publish(self):
        self.is_published = True

    def set_unpublish(self):
        self.is_published = False


class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    # survey_id = fields.Many2one('survey.survey', related='job_id.survey_id', string="Survey", readonly=True)
