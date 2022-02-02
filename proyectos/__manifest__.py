# -*- coding: utf-8 -*-
{
    'name': "Gestión de proyectos",

    'summary': """
        Modulo de ejemplo para SGE""",

    'description': """
        Este módulo pretende ser una guía para la programación 
        y desarrollo de módulos en Odoo
    """,

    'author': "Rafa SaliNipon",
    'website': "http://infsalinas.sytes.net:10445",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'UnaModerna',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # Es una aplicación
    'application' : True ,
}
