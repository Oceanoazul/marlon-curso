from odoo import models, fields, api

class pets(models.Model):
    _name = 'ej.pets'
    
    name = fields.Char(string='name', required=True)
    age = fields.Integer(string='age')
    color = fields.Char(string='color')
    type = fields.Selection([('small', 'Small'),
                            ('medium', 'Medium'), 
                            ('big', 'Big')], string='Type', default='small', required=True)
    