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
    
    
    def populate(self) -> None:
        """
        Populates the Bio2BEL OmniPath database.
        """
        
        log.info('Populating database.')
        
        interactions = parser.get_interactions()
        ptms = parser.get_ptms()
        
        log.info('Building models.')
        
        for (
            source, target, source_genesymbol, target_genesymbol,
            is_directed, is_stimulation, is_inhibition,
            dip_url, sources, references
        ) in interactions.itertuples():
            
            models.Protein(
                uniprot_id = ,
                gene_name = ,
            )
            
            models.Interaction(
                
            )
    
    
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
    
    
    
