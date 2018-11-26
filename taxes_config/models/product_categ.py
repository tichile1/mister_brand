from odoo import models, fields, api, tools

class ProductCategory(models.Model):
    _inherit = "product.category"

    taxes = fields.One2many(
        'account.tax',
        'categories',
        string="Taxes"
    )
