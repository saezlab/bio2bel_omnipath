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

import collections

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
    
    
    def is_populated(self):
        """
        Checks if the Bio2BEL OmniPath database is populated.
        """
        
        return self.count_interactions() > 0 and self.count_ptms() > 0
    
    
    def summarize(self):
        """
        Summarizes the contents of the Bio2BEL OmniPath database.
        """
        
        return dict(
            interactions = self.count_interactions(),
            ptms = self.count_ptms(),
            proteins = self.count_proteins(),
        )
    
    
    def populate(self):
        """
        Populates the Bio2BEL OmniPath database.
        """
        
        self.populate_interactions()
        self.populate_ptms()
    
    
    def populate_interactions(self):
        
        log.info('Populating database.')
        
        interactions = parser.get_interactions()
        
        
        log.info('Building models.')
        
        int_type_to_entity_type = {
            'PPI': ('protein', 'protein'),
            'TF': ('protein', 'protein'),
            'MTI': ('mirna', 'protein'),
            'TFM': ('protein', 'mirna'),
        }
        
        self.interactions_by_partners = collections.defaultdict(list)
        self.interactions_d = {}
        self.interaction_types_d = {}
        self.entities_d = {}
        self.entity_types_d = {}
        self.references_d = {}
        self.taxons_d = {}
        self.resources_d = {}
        self.ptms_d = {}
        self.mod_types_d = {}

        
        for (
            source, target, source_genesymbol, target_genesymbol,
            is_directed, is_stimulation, is_inhibition,
            dip_url, resources, references, typ, source_taxid, target_taxid,
        ) in interactions.itertuples():
            
            source_type, target_type = int_type_to_entity_type[typ]
            
            # creating the entities
            source_entity_i = self.insert_entity(
                primary_id = source,
                secondary_id = source_genesymbol,
                taxid = source_taxid,
                entity_type = source_type,
            )
            
            target_entity_i = self.insert_entity(
                primary_id = target,
                secondary_id = target_genesymbol,
                taxid = target_taxid,
                entity_type = target_type,
            )
            
            interaction_type_i = self.insert(
                d = self.interaction_types_d,
                key = typ,
                model = models.InteractionType,
                interaction_type = typ,
            )
            
            # creating the interaction
            interaction_key = (
                source, target, is_directed,
                is_stimulation, is_inhibition,
                typ,
            )
            
            interaction_i = self.insert(
                d = self.interactions_d,
                key = interaction_key,
                model = models.Interaction,
                source = source_entity_i,
                target = target_entity_i,
                is_directed = is_directed,
                is_stimulation = is_stimulation,
                is_inhibition = is_inhibition,
                type = interaction_type_i,
            )
            
            partners = [source, target]
            
            if not is_directed:
                
                partners.sort()
            
            partners.append(typ)
            
            self.interactions_by_partners[tuple(partners)].append(
                interaction_i
            )
            
            # creating references and resources
            for pubmed_id in references.split(';'):
                
                reference_i = self.insert(
                    d = self.references_d,
                    key = pubmed_id,
                    model = models.Reference,
                    pubmed_id = pubmed_id,
                )
                
                interaction.references.append(reference_i)
            
            for resource in resources.split(;):
                
                resource_i = self.insert(
                    d = self.resources_d,
                    key = resource,
                    model = models.Resource,
                    resource_name = resource,
                )
                
                interaction.resources.append(resource_i)
    
    
    def populate_ptms(self):
        
        ptms = parser.get_ptms()
        
        for (
            source, target,
            source_genesymbol, target_genesymbol,
            residue_type, residue_offset, modification,
            resources, references, taxid,
        ) in ptms.itertuples():
            
            # creating the entities
            source_entity_i = self.insert_entity(
                primary_id = source,
                secondary_id = source_genesymbol,
                taxid = source_taxid,
                entity_type = source_type,
            )
            
            target_entity_i = self.insert_entity(
                primary_id = target,
                secondary_id = target_genesymbol,
                taxid = target_taxid,
                entity_type = target_type,
            )
            
            mod_type_i = self.insert(
                d = self.mod_types_d,
                key = modification,
                model = models.PtmType,
                ptm_type = modification,
            )
            
            ptm_key = (source, target, residue_type, residue_offset)
            
            ptm_i = self.insert(
                d = ptms_d,
                key = ptm_key,
                model = models.Ptm,
                source_id = source_entity_i,
                target_id = target_entity_i,
                sequence_offset = residue_offset,
                residue_type = residue_type,
                modification_type = mod_type_i,
            )
            
            # references to interactions
            partners_key = (source, target, 'PPI')
            
            for interaction_i in self.interactions_by_partners[partners_key]:
                
                ptm.interactions.append(interaction_i)
            
            # creating references and resources
            for pubmed_id in references.split(';'):
                
                reference_i = self.insert(
                    d = self.references_d,
                    key = pubmed_id,
                    model = models.Reference,
                    pubmed_id = pubmed_id,
                )
                
                ptm.references.append(reference_i)
            
            for resource in resources.split(;):
                
                resource_i = self.insert(
                    d = self.resources_d,
                    key = resource,
                    model = models.Resource,
                    resource_name = resource,
                )
                
                ptm.resources.append(resource_i)
    
    
    def insert_entity(self, primary_id, secondary_id, taxid, entity_type):
        
        entity_type_i = self.insert(
            d = self.entity_types_d,
            key = entity_type,
            model = models.EntityType,
            entity_type = entity_type,
        )
        
        taxon_i = self.insert(
            d = self.taxons_d,
            key = taxid,
            model = models.Taxonomy,
            ncbi_taxonomy_id = taxid,
        )
        
        entity_i = self.insert(
            d = self.entities_d,
            key = entity,
            model = models.MolecularEntity,
            primary_id = primary_id,
            secondary_id = secondary_id,
            taxon = taxon_i,
            type = entity_type_i,
        )
        
        return entity_i
    
    
    @staticmethod
    def insert(d, key, model, append = False, **kwargs):
        """
        Inserts a record into a table and returns the instance.
        It also inserts the instance into the dict ``d`` with key ``key``.
        If the record already exists does nothing but returns the instance.
        Field names and values should be provided as ``**kwargs``.
        The ``model`` is the ``sqlalchemy`` table model to use.
        """
        
        if key not in d:
            
            d[key] = model(**kwargs)
        
        return d[key]
    
    
    def count_interactions(self):
        """
        Counts the number of interactions in the database.
        """
        
        return self._count_model(Interaction)
    
    
    def count_ptms(self):
        """
        Counts the number of enzyme-substrate relationships in the database.
        """
        
        return self._count_model(Ptm)
    
    
    def count_proteins(self):
        """
        Counts the number of proteins in the database.
        """
        
        return self._count_model(Protein)
    
    
    
