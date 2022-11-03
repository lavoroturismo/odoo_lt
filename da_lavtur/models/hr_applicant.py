
import logging
from odoo import fields,models,api,_
from datetime import date, timedelta
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    partner_surname     = fields.Char(string='Cognome candidato', required = True)
    codice_lt           = fields.Integer( string = 'Codice LT', required = False, default = None )
    data_nascita        = fields.Date( string = 'Data di nascita', required = False, default = None )
    ultimo_contatto     = fields.Date( string = 'Ultimo contatto', required = False, default = None )
    age                 = fields.Integer( compute = 'compute_age', store=False )
    preferenze_esigenze = fields.Text( string="Preferenze e Esigenze", required = False, default = None )
    info_candidato      = fields.Text( string="Info Candidato", required = False, default = None )
    info_lavoro         = fields.Text( string="Info Lavoro", required = False, default = None )
   #priority            = fields.Selection( selection_add = [ ('4', 'Fourth'), ('5', 'Fifth') ] )
    valutazione         = fields.Integer( string="Valutazione", default = 0 )
    affidabilita        = fields.Integer( string="Affidabilità", default = 0 )
   #affidabilita        = fields.Selection( [ ('0', 'Zero'), ('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'), ('5', 'Fifth') ], string="Affidabilità" )
    valutazioni_interne = fields.Text( string="Valutazioni Interne", required = False, default = None )
    valutazione_finale  = fields.Text( string="Valutazione Finale", required = False, default = None )
    mansione_ruolo      = fields.Many2many('hr.department', 'hr_applicant_department', 'applicant_id', 'department_id', string='Mansione-Ruolo', required = False, default = None)
    referenze           = fields.Text( string="Referenze", required = False, default = None )
    feedback_aziende    = fields.Text( string="Feedback Aziende", required = False, default = None )
    piazzato            = fields.Boolean( string='Piazzato', default = False)

    def name_get(self):
        result = []
        for applicant in self:
            #if applicant.partner_name:
            #    name = applicant.partner_name
            #else:
            #    name = applicant.name
            name = applicant.name
            result.append((applicant.id, name))
        return result

    @api.model
    def create( self, vals ):
        vals['name'] = vals['partner_name'] + ' ' + vals['partner_surname']
        applicant = super( HrApplicant, self ).create( vals )
        return applicant

    def write( self, vals ):
        if 'partner_name' in vals.keys() or 'partner_surname' in vals.keys():
            applicant = self.env['hr.applicant'].search( [ ( 'id', '=', self.id ) ], limit = 1 )
            vals['name'] = vals['partner_name'] if 'partner_name' in vals.keys() else self.partner_name
            vals['name'] += ' '
            vals['name'] += vals['partner_surname'] if 'partner_surname' in vals.keys() else self.partner_surname
        applicant = super( HrApplicant, self ).write( vals )
        return applicant

    @api.depends('data_nascita')
    def compute_age(self):
        #_logger.info( 'data_nascita ' + str( self.data_nascita ) );
        if self.data_nascita == False:
            self.age = None
        else:
            self.age = ( date.today() - self.data_nascita ) // timedelta( days = 365.2425 )


    @api.constrains( 'valutazione' )
    def check_input_val(self):
        """ un numero intero da 0 a 10 """
        min = 0
        max = 10
        if self.valutazione < min or self.valutazione > 10:
            raise ValidationError(_('La valutazione deve essere compresa tra 0 e 10'))
        return True


    @api.constrains( 'affidabilita' )
    def check_input_aff(self):
        """ un numero intero da 0 a 10 """
        min = 0
        max = 10
        if self.affidabilita < min or self.affidabilita > 10:
            raise ValidationError(_('L\'affidabilità deve essere compresa tra 0 e 10'))
        return True

