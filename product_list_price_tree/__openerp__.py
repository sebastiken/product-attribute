# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2016 E-MIPS (http://www.e-mips.com.ar)
#    All Rights Reserved. See AUTHORS for details.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
    'name': 'Update List Price Tree view',
    'version': '8.0.1.0.0',
    'author': 'E-MIPS, Odoo Community Association (OCA)',
    'summarize': 'Update list price of products from Tree View',
    'maintainer': 'E-MIPS',
    'category': 'sale',
    'depends': [
        'sale',
    ],
    'website': 'http://www.e-mips.com.ar/',
    'data': [
        'product_view.xml',
    ],
    'demo': [
    ],
    'tests': [],
    'images': [
    ],
    'installable': True,
    'license': 'AGPL-3',
    'external_dependencies': {
        'python': [],
    },
}
