from odoo import models, fields, api

class pets(models.Model):
    _name = 'ej.pets'
    
    name = fields.Char(string='name', required=True)
    code = fields.Char(string='code', default='New', readonly=1)
    age = fields.Integer(string='age')
    color = fields.Char(string='color')
    type = fields.Selection([('small', 'Small'),
                            ('medium', 'Medium'), 
                            ('big', 'Big')], string='Type', default='small', required=True)

    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code('ej.pets') or 'New'
        return super(pets, self).create(vals)