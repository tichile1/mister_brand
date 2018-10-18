from odoo import api, fields, models, tools

class ProductTaxes(models.Model):
    _inherit = "account.tax"

    applies_on = fields.One2Many(
        'product.category',
        string="Aplica a:"    
    )
