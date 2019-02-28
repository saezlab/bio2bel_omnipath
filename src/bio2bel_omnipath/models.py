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

import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

import pybel

from .constants import MODULE_NAME

__all__ = [
    'Base',
]

logger = logging.getLogger(__name__)


PROTEIN_TABLE_NAME = f'{MODULE_NAME}_protein'
INTERACTION_TABLE_NAME = f'{MODULE_NAME}_interaction'
PTM_TABLE_NAME = f'{MODULE_NAME}_ptm'


Base: sqlalchemy.ext.declarative.DeclarativeMeta = (
    sqlalchemy.ext.declarative.declarative_base()
)


class Protein(Base):
    """
    Represents a protein.
    """
    
    __tablename__ = PROTEIN_TABLE_NAME
    
    id = sqlalchemy.Column(Integer, primary_key = True)
    
    taxonomy_id = Column()
