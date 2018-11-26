from odoo import models, fields, api, tools

class ProductTemplate(models.Model):
    _inherit="product.template"

    @api.onchange('categ_id', 'categ_id.taxes')
    def add_taxes(self):
        for record in self:
            record.write({
                'taxes_id': [(6, tax.id, None) for tax in record.categ_id.taxes],
                })
                
