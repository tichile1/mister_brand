# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class tdt_tichile_cl_dte(models.Model):
#     _name = 'tdt_tichile_cl_dte.tdt_tichile_cl_dte'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100