

{
    'name': 'Hr Recruitment Module',
    'version': '14.0.1.1.1',
    'summary': """Recruitment Module""",
    'description': """This module helps recruitment organization to maintain their client and applicant and job position
    in a way that they will able to do their job effortlessly
    """,
    'author': 'Geotechnosoft',
    'depends': ['base', 'hr','hr_recruitment','mail'],
    # 'assets': {
    #           "web.assets_backend": [
    #                 "odoo_web_login/static/src/css/web_login_style.css"
    #                 "web/static/src/core/network/rpc_service.js"
    #                 # "hr_applicant/static/src/js/min.js"
    #             ]
    # },

    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'report/recruitment_report_view.xml',
        'views/hr_applicant_view.xml',
        'views/hr_recruitment.xml',
        'views/hr_stage_view.xml',
        'views/job_position_stage_view.xml',
        'views/hr_token_key_view.xml',
        'views/res_partner_view.xml',
        'views/template.xml',
        'wizard/pdf_attachment_view.xml',
        'wizard/candidate_resume_attachment_view.xml',
        'wizard/candidate_profile_view.xml',
        'wizard/applicant_wizard_view.xml',
        'wizard/message_wizard.xml',
        # 'wizard/applicant_multiple_wizard_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
