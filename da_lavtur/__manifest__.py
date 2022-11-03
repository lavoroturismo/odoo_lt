# -*- coding: utf-8 -*-

{
    'name': 'Lavoro Turismo Integrations',
    'version': '1.0.0',
    'category': 'Recrutiment',
    'author': 'Digital Automations',
    'description': """
LAVORO TURISMO INTEGRATIONS  
---------------------------

""",
    'summary': 'Recruitment Module for Lavoro Turismo',
    'depends': [ 'base', 'geo_recruitment', 'l10n_it_fatturapa' ],
    #'assets': {
    #    'web.assets_backend': [
    #        'ko_aves/static/src/js/*.js',
    #    ],
    #},
    'data': [  # per importare i file xml csv
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/hr_job.xml',
        'views/hr_recruitment.xml',
        'views/hr_contract_type.xml',
        #'views/hr_applicant.xml',
        'wizard/candidate_resume_attachment_view.xml',
    ],
    'demo': [], # per importare dati demo
    'sequence': -100,
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3'
}

