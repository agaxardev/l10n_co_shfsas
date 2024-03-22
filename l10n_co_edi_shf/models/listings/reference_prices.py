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

from odoo import models

_logger = logging.getLogger(__name__)


class ReferencePrices(models.Model):
    _name = "l10n_co_edi_shf.reference_prices"
    _inherit = "l10n_co_edi_shf.languages"
    _description = "Reference prices"
