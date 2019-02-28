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
SQLAlchemy models for Bio2BEL OmniPath.
"""

import logging

from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

__all__ = [
    'Base',
]

logger = logging.getLogger(__name__)

Base: DeclarativeMeta = declarative_base()
