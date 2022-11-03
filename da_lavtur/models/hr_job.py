
from odoo import fields,models,api,_


class HrJob(models.Model):
    _inherit = 'hr.job'

    # sotto a user_id
    user_ext_id = fields.Many2one('res.users', 'Selezionatore Esterno', tracking=True, default= lambda self : self.env.user)

    contract_type_id = fields.Many2one('hr.contract.type', 'Tipo di Contratto', required = False, default = None)
    
    # sotto a ufficio
    # qualifica # TODO
    descrizione_qualifica = fields.Char(string='Descrizione Qualifica', required=False, default = None)
    qualifica             = fields.Many2one('hr.department', string='Qualifica', required = False, default = None)

    # box a parte
    motivo_reclutamento = fields.Char(string='Motivo del recluitamento', required=False, default = None)
    inizio_fine_impiego = fields.Char(string='Inizio/Fine impiego', required=False, default = None)
    retribuzione        = fields.Char(string='Retribuzione', required=False, default = None)
    orari               = fields.Char(string='Orari', required=False, default = None)
    divisa              = fields.Char(string='Divisa e lavaggio', required=False, default = None)
    alloggio            = fields.Char(string='Alloggio', required=False, default = None)
    benefit             = fields.Char(string='Benefit', required=False, default = None)
    altro               = fields.Text(string='Altro', required=False, default = None)

    # tab Descrizione
    compiti             = fields.Text(string='Descrizione Lavoro', required=False, default = None)

    # tab Profilo Ideale
    eta                 = fields.Char(string='Età', required=False, default = None)
    sesso               = fields.Char(string='Sesso', required=False, default = None)
    residenza_domicilio = fields.Char(string='Residenza / Domicilio', required=False, default = None)
    formazione          = fields.Text(string='Formazione e studi', required=False, default = None)
    auto_patente        = fields.Char(string='Auto / patente', required=False, default = None)
    requisiti           = fields.Text(string='Requisiti', required=False, default = None)
    dati_quantitativi   = fields.Char(string='Dati quantitativi', required=False, default = None)
    lingue              = fields.Text(string='Conoscenze linguistiche', required=False, default = None)
    tipo_esperienze     = fields.Text(string='Esperienza', required=False, default = None)
    skills              = fields.Text(string='Skills', required=False, default = None)
    punti_forza         = fields.Text(string='Punti forza', required=False, default = None)
    punti_critici       = fields.Text(string='Punti critici', required=False, default = None)
    situazione          = fields.Text(string='Situazione', required=False, default = None)
    annuncio            = fields.Text(string='Annuncio', required=False, default = None)

    no_of_recruitment   = fields.Integer( string="N. di Posizioni", default=1 )
    expected_closing_date = fields.Date( string="Data di chiusura", required = False )
