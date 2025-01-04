from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    date_deadline = fields.Date(string="Fecha Límite")

