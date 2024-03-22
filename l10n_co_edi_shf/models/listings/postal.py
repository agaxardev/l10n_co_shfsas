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

import logging

from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class Postal(models.Model):
    _name = "l10n_co_edi_shf.postal"
    _description = "Postal"

    name = fields.Char(string="Postal code", required=True)
    postal_zone = fields.Char(string='Postal zone', required=True)
    municipality_id = fields.Many2one(comodel_name='l10n_co_edi_shf.postal_municipality', string='Municipality',
                                      required=True, index=True)
    department_id = fields.Many2one(comodel_name='l10n_co_edi_shf.postal_department', string='Department',
                                    required=True, index=True)
    type = fields.Char(string='Type', required=True)
    neighborhood = fields.Char(string='Neighborhood', required=True)
    sidewalk = fields.Char(string='Sidewalk', required=True)
