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
ENTITY_TYPE_TABLE_NAME = '%s_entity_type' % MODULE_NAME
INTERACTION_TYPE_TABLE_NAME = '%s_interaction_type' % MODULE_NAME
PTM_TYPE_TABLE_NAME = '%s_ptm_type' % MODULE_NAME

ASSOC_INT_REF_TABLE_NAME = '%s_interaction_reference' % MODULE_NAME
ASSOC_INT_RES_TABLE_NAME = '%s_interaction_resource' % MODULE_NAME
ASSOC_ENT_TAX_TABLE_NAME = '%s_entity_taxonomy' % MODULE_NAME
ASSOC_INT_PTM_TABLE_NAME = '%s_interaction_ptm' % MODULE_NAME

ASSOC_PTM_REF_TABLE_NAME = '%s_ptm_reference' % MODULE_NAME
ASSOC_PTM_RES_TABLE_NAME = '%s_ptm_resource' % MODULE_NAME

ASSOC_RES_REF_TABLE_NAME = '%s_resource_reference' % MODULE_NAME


Base = sqlalchemy.ext.declarative.declarative_base()

#
# Association tables
#

assoc_res_ref = sqlalchemy.Table(
    ASSOC_RES_REF_TABLE_NAME,
    Base.metadata,
    sqlalchemy.Column(
        'resource_id',
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('%s.id' % RESOURCE_TABLE_NAME),
    ),
    sqlalchemy.Column(
        'reference_id',
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('%s.id' % REFERENCE_TABLE_NAME),
    ),
)


assoc_int_ref = sqlalchemy.Table(
    ASSOC_INT_REF_TABLE_NAME,
    Base.metadata,
    sqlalchemy.Column(
        'interaction_id',
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('%s.id' % INTERACTION_TABLE_NAME),
    ),
    sqlalchemy.Column(
        'reference_id',
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('%s.id' % REFERENCE_TABLE_NAME),
    ),
)


assoc_int_res = sqlalchemy.Table(
    ASSOC_INT_RES_TABLE_NAME,
    Base.metadata,
    sqlalchemy.Column(
        'interaction_id',
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('%s.id' % INTERACTION_TABLE_NAME),
    ),
    sqlalchemy.Column(
        'resource_id',
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('%s.id' % RESOURCE_TABLE_NAME),
    ),
)


assoc_int_ptm = sqlalchemy.Table(
    ASSOC_INT_PTM_TABLE_NAME,
    Base.metadata,
    sqlalchemy.Column(
        'interaction_id',
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('%s.id' % INTERACTION_TABLE_NAME),
    ),
    sqlalchemy.Column(
        'ptm_id',
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('%s.id' % PTM_TABLE_NAME),
    ),
)


assoc_ent_tax = sqlalchemy.Table(
    ASSOC_ENT_TAX_TABLE_NAME,
    Base.metadata,
    sqlalchemy.Column(
        'molecular_entity_id',
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('%s.id' % INTERACTION_TABLE_NAME),
    ),
    sqlalchemy.Column(
        'taxonomy_id',
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('%s.id' % TAXONOMY_TABLE_NAME),
    ),
)

#
# Entity tables
#

class MolecularEntity(Base):
    """
    Represents a protein.
    """
    
    __tablename__ = PROTEIN_TABLE_NAME
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    
    primary_id = sqlalchemy.Column(
        sqlalchemy.String(16),
        nullable = False,
        index = True,
        unique = True,
        doc = 'UniProtKB ID or miRBase mature miRNA AC',
    )
    
    secondary_id = sqlalchemy.Column(
        sqlalchemy.String(24),
        nullable = False,
        index = True,
        doc = 'Primary Gene Symbol or miRBase mature miRNA name',
    )
    
    taxonomy_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('%s.id' % TAXONOMY_TABLE_NAME),
        nullable = False,
        index = True,
        doc = 'Key of the taxon of the molecular entity.',
    )
    
    taxon = sqlalchemy.orm.relationship(
        TAXONOMY_TABLE_NAME,
    )
    
    type = sqlalchemy.orm.relationship(
        ENTITY_TYPE_TABLE_NAME,
    )


class EntityType(Base):
    """
    Describes types of molecular entities.
    """
    
    __tablename__ = ENTITY_TYPE_TABLE_NAME
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    
    entity_type = sqlalchemy.Column(
        sqlalchemy.String(8),
        nullable = False,
        index = True,
        unique = True,
        doc = 'Type of a molecular entity',
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
        unique = True,
        doc = 'NCBI Taxonomy ID',
    )


class Interaction(Base):
    """
    Represents an interaction between molecular entities.
    """
    
    __tablename__ = INTERACTION_TABLE_NAME
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    
    #
    # Basic interaction (graph) data
    #
    
    source_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('%s.id' % ENTITY_TABLE_NAME),
        nullable = False,
        index = True,
        doc = 'Key of the source MolecularEntity',
    )
    
    target_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('%s.id' % ENTITY_TABLE_NAME),
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
    
    type = sqlalchemy.relationship(
        INTERACTION_TYPE_TABLE_NAME,
    )
    
    #
    # Interaction annotations
    #
    
    resources = sqlalchemy.orm.relationship(
        RESOURCE_TABLE_NAME,
        secondary = assoc_int_ref,
    )
    
    references = sqlalchemy.orm.relationship(
        REFERENCE_TABLE_NAME,
        secondary = assoc_int_ref,
    )
    
    references = sqlalchemy.orm.relationship(
        REFERENCE_TABLE_NAME,
        secondary = assoc_int_ptm,
    )
    
    ptms = sqlalchemy.orm.relationship(
        PTM_TABLE_NAME,
        secondary = assoc_int_ptm,
    )


class InteractionType(Base):
    """
    Describes types of interactions.
    """
    
    __tablename__ = INTERACTION_TYPE_TABLE_NAME
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    
    entity_type = sqlalchemy.Column(
        sqlalchemy.String(18),
        nullable = False,
        index = True,
        unique = True,
        doc = 'Category of an interaction',
    )


class Ptm(Base):
    """
    Represents a post-translational modification.
    """
    
    __tablename__ = PTM_TABLE_NAME
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    
    source_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('%s.id' % ENTITY_TABLE_NAME),
        nullable = False,
        index = True,
        doc = 'Key of the source MolecularEntity',
    )
    
    target_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('%s.id' % ENTITY_TABLE_NAME),
        nullable = False,
        index = True,
        doc = 'Key of the target MolecularEntity',
    )
    
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
    
    modification_type = sqlalchemy.orm.relationship(
        PTM_TYPE_TABLE_NAME,
    )
    
    references = sqlalchemy.orm.relationship(
        REFERENCE_TABLE_NAME,
        secondary = assoc_int_ptm,
    )
    
    interactions = sqlalchemy.orm.relationship(
        INTERACTION_TABLE_NAME,
        secondary = assoc_int_ptm,
    )


class PtmType(Base):
    """
    Describes types of a PTM e.g. phosphorylation, acetylation.
    """
    
    __tablename__ = PTM_TYPE_TABLE_NAME
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    
    entity_type = sqlalchemy.Column(
        sqlalchemy.String(24),
        nullable = False,
        index = True,
        unique = True,
        doc = 'Type of a PTM, e.g. phosphorylation, acetylation...',
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
        unique = True,
        doc = 'PubMed ID',
    )


class Resource(Base):
    """
    Represents a database (resource).
    """
    
    __tablename__ = RESOURCE_TABLE_NAME
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    
    resource_name = sqlalchemy.Column(
        sqlalchemy.String(24),
        nullable = False,
        index = True,
        unique = True,
        doc = 'Database',
    )
    
    reference = sqlalchemy.orm.relationship(
        REFERENCE_TABLE_NAME,
    )
