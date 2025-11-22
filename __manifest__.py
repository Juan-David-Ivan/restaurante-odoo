# -*- coding: utf-8 -*-
{
    'name': "restaurante",

    'summary': "Gestion de un restaurante",

    'description': """
Proyecto realizado por Juan David
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'reports/plato_report.xml',
        'views/views.xml',
        'views/templates.xml',
    ],

    'aplication':True,
    'intallable':True,
    'autoinstall':False,
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

