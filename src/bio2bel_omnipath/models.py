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


ENTITY_TABLE_NAME = '%s_molecular_entity' % MODULE_NAME
INTERACTION_TABLE_NAME = '%s_interaction' % MODULE_NAME
PTM_TABLE_NAME = '%s_ptm' % MODULE_NAME
TAXONOMY_TABLE_NAME = '%s_taxonomy' % MODULE_NAME
RESOURCE_TABLE_NAME = '%s_resource' % MODULE_NAME
REFERENCE_TABLE_NAME = '%s_reference' % MODULE_NAME


Base = sqlalchemy.ext.declarative.declarative_base()


class MolecularEntity(Base):
    """
    Represents a protein.
    """
    
    __tablename__ = PROTEIN_TABLE_NAME
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    
    primary_id = sqlalchemy.Comumn(
        sqlalchemy.String(16),
        nullable = False,
        index = True,
        doc = 'UniProtKB ID or miRBase mature miRNA AC',
    )
    
    secondary_id = sqlalchemy.Comumn(
        sqlalchemy.String(24),
        nullable = False,
        index = True,
        doc = 'Primary Gene Symbol or miRBase mature miRNA name',
    )


class Interaction(Base):
    """
    Represents an interaction between molecular entities.
    """
    
    __tablename__ = INTERACTION_TABLE_NAME
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    
    source_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable = False,
        index = True,
        doc = 'Key of the source MolecularEntity',
    )
    
    target_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable = False,
        index = True,
        doc = 'Key of the target MolecularEntity',
    )
    
    is_directed = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable = False,
        index = True,
        doc = 'Boolean: the interaction is directed',
    )
    
    is_stimulation = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable = False,
        index = True,
        doc = 'Boolean: the interaction has stimulatory effect',
    )
    
    is_inhibition = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable = False,
        index = True,
        doc = 'Boolean: the interaction has inhibitory effect',
    )


class Taxonomy(Base):
    """
    Represents taxons identified by NCBI Taxonomy IDs.
    """
    
    __tablename__ = TAXONOMY_TABLE_NAME
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    
    ncbi_taxonomy_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable = False,
        index = True,
        doc = 'NCBI Taxonomy ID',
    )


class Ptm(Base):
    """
    Represents a post-translational modification.
    """
    
    __tablename__ = PTM_TABLE_NAME
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    
    sequence_offset = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable = False,
        index = True,
        doc = 'Sequence position of the modified residue',
    )
    
    residue_type = sqlalchemy.Column(
        sqlalchemy.String(1),
        nullable = False,
        index = True,
        doc = 'Single letter code of the modified residue',
    )
    
    modification_type = sqlalchemy.Column(
        sqlalchemy.String(24),
        nullable = False,
        index = True,
        doc = 'Modification type',
    )
    
    uniprot_id = sqlalchemy.Column(
        sqlalchemy.String(10),
        nullable = False,
        index = True,
        doc = 'UniProtKB ID of the modified protein',
    )


class Reference(Base):
    """
    Represents a literature reference identified by PubMed ID.
    """
    
    __tablename__ = REFERENCE_TABLE_NAME
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    
    pubmed_id = sequence_offset = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable = False,
        index = True,
        doc = 'PubMed ID',
    )


class Resource(Base):
    """
    Represents a database (resource).
    """
    
    __tablename__ = RESOURCE_TABLE_NAME
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    
    pubmed_id = sequence_offset = sqlalchemy.Column(
        sqlalchemy.String(24),
        nullable = False,
        index = True,
        doc = 'Database',
    )
