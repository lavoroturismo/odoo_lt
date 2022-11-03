# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartnerType(models.Model):
    _name = 'hr.contract.type'
    _description = 'Tipologie di Contratto'
    _rec_name = 'label'

    label       = fields.Char( string = 'Nome', required = True )
    description = fields.Text( string = 'Descrizione', required = False, default = None )


