# -*- coding: utf-8 -*-
#
# shf S.A.S. - Copyright (2019-2022)
#
# This file is part of l10n_co_edi_shf.
#
# l10n_co_edi_shf is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# l10n_co_edi_shf is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with l10n_co_edi_shf.  If not, see <https://www.gnu.org/licenses/>.
#
# email: info@shf.com.co
#

from odoo import fields, models


class AccountTax(models.Model):
    _inherit = "account.tax"

    edi_tax_id = fields.Many2one('l10n_co_edi_shf.taxes', string="Tax type (DIAN)", ondelete='RESTRICT', copy=True)

    dian_report_tax_base = fields.Selection([
        ('auto', 'Auto'),
        ('no_report', 'Not reporting the taxable base to the DIAN')
    ], string="Taxable base (DIAN)", default='auto', copy=True)
