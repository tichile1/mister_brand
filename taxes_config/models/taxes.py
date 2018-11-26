from odoo import api, fields, models, tools

class Tax(models.Model):
    _inherit = "account.tax"

    categories = fields.Many2one(
        'product.category',
        string="Categories",
    )
