# -*- coding: utf-8 -*-
{
    'name': u"Mr.Brand Modifications",

    'summary': """
        Mr.Brand Priclist Modification
        """,

    'description': u"""
        Módulo que implementa modificaciones a los pricelist""",

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'tdt',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account, product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/tax_config.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'OPL-1',
}
