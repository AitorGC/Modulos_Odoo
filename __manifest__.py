# -*- coding: utf-8 -*-
{
    'name': "Gestion de Piezas",

    'summary': """
        Modulo que hace la gestion de piezas y las asigna a un empleado""",

    'description': """
        Este modulo da de alta las piezas que llegan al almacen y las asigna a un empleado
    """,

    'author': "Aitor Santana",
    'website': "http://www.aitorsantana.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Gestion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/piezas.xml',
        'views/empleados.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}