# -*- coding: utf-8 -*-
{
    'name': "many2many",

    'summary': """
        about the many2many""",

    'description': """
        Long description of module's purpose
    """,

    'author': "zoubida ",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'view.xml',
	'record.xml',
    ],
}
