
from odoo import fields,models,api,_


class ResPartner(models.Model):
    _inherit = 'res.partner'
    #_rec_name = 'res_partner_label'

    #user_id = fields.Many2one('res.users', string='Account Manager',
    #                          help='The internal user in charge of this contact.')

    ragione_sociale = fields.Char( string = 'Ragione Sociale', required = False, default = None )
    referenti_interni_ids = fields.Many2many( 'res.users', string = 'Referenti interni' )

    # tab Location/Alloggi
    info_location = fields.Text( string = 'Info Location', required = False, default = None )
    alloggio = fields.Text( string = 'Alloggio', required = False, default = None )

    # tab L'Azieda
    l_azienda = fields.Text( string = 'L\'azienda', required = False, default = None )
    azienda_personale = fields.Text( string = 'Azienda-Personale', required = False, default = None )

    # tab punti forza / critici
    punti_forza = fields.Text( string = 'Punti di Forza', required = False, default = None )
    punti_critici = fields.Text( string = 'Punti Critici', required = False, default = None )

    insegna = fields.Char( string = 'Insegna', required = False, default = None )

    sdi = fields.Char( string = 'SDI', store = False, related = "codice_destinatario" )

    #res_partner_label = fields.Char( string = 'res_partner_label', compute = 'compute_res_partner_label', store = False )

    #@api.multi
    def name_get( self):
        res = []
        for field in self:
            if field.insegna == field.name:
                res.append( ( field.id, field.insegna ) )
            elif field.insegna:
                res.append( ( field.id, '%s [%s]' % ( field.insegna, field.name ) ) )
            else:
                res.append( ( field.id, field.name ) )
        return res

    @api.depends('codice_destinatario')
    def compute_sdi(self):
        for each in self:
            each.sdi  = each.codice_destinatario

    @api.depends('name', 'insegna')
    def compute_res_partner_label(self):
        res = None
        if self.insegna == self.name:
            res = self.insegna
        elif self.insegna:
            res = '%s [%s]' % ( self.insegna, self.name )
        else:
            res = self.name
        return res
