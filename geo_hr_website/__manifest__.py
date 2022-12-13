{
    'name': 'Hr Recruitment Website',
    'version': '14.0.1.1.1',
    'summary': """Employee Document""",
    'description': """Employee Document""",
    'author': 'Geotechnosoft',
    'depends': ['base', 'hr_recruitment','mail','website_hr_recruitment','geo_recruitment'],
    # 'assets': {
    #           "web.assets_backend": [
    #                 "odoo_web_login/static/src/css/web_login_style.css"
    #                 "web/static/src/core/network/rpc_service.js"
    #                 # "hr_applicant/static/src/js/min.js"
    #             ]
    # },

    'data': [
        # 'security/ir.model.access.csv',
        'views/hr_job_views.xml',
        # 'wizard/applicant_multiple_wizard_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}