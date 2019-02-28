#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  This file is part of the `bio2bel_omnipath` python module
#
#  Copyright (c) 2019
#  Uniklinik RWTH Aachen
#  Heidelberg University
#
#  File author(s): Dénes Türei (turei.denes@gmail.com)
#
#  Distributed under the MIT License.
#  See accompanying file LICENSE or copy at
#      https://spdx.org/licenses/MIT.html
#
#  Website: http://omnipathdb.org/
#

"""
Manager for Bio2BEL OmniPath.
"""

import bio2bel
from .constants import MODULE_NAME
import .models
import .parser

__all__ = [
    'Manager',
]

class Manager(bio2bel.AbstractManager):
    """
    Manages the Bio2BEL OmniPath database.
    """

    module_name = MODULE_NAME
    _base = models.Base

    def is_populated(self) -> bool:
        """Check if the Bio2BEL OmniPath database is populated."""
        raise NotImplementedError

    def summarize(self) -> Mapping[str, int]:
        """Summarize the contents of the Bio2BEL OmniPath database."""
        raise NotImplementedError

    def populate(self) -> None:
        """Populate the Bio2BEL OmniPath database."""
        raise NotImplementedError
