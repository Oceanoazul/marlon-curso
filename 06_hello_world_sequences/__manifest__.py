##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2018 Marlon Falcon Hernandez
#    (<http://www.marlonfalcon.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': '06 Hello World Data',
    'version': '16.0.1.0.0',
    'author': 'Nachete',
    'mantainer': 'Nachete',
    'website': 'https://www.expansionoceanoazul.com',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'summary': 'A module for translating Hello World',
    'description': """
        This module provides translations for the Hello World message.
    """,
    'depends': ['base'],
    'data': [
        'views/pet_views.xml',
        'security/ir.model.access.csv',
        'data/pet_data.xml',
        'data/ir_sequence.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    
    'images': ['static/description/icon.png'],
}