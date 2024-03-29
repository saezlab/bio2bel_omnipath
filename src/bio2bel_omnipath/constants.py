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
Constants for Bio2BEL OmniPath.
"""

import os

import bio2bel


__all__ = [
    'VERSION',
    'MODULE_NAME',
    'DATA_DIR',
    'get_version',
]

VERSION = '0.0.1'
MODULE_NAME = 'omnipath'
DATA_DIR = bio2bel.get_data_dir(MODULE_NAME)
DEFAULT_CONNECTION = bio2bel.get_connection(MODULE_NAME)

PROTEIN_NAMESPACE = 'UNIPROT'

OMNIPATH_URL = (
    'http://omnipathdb.org/%s/?'
    'fields=sources,references%s,ncbi_tax_id&gensymbols=1'
)
INTERACTIONS_URL = OMNIPATH_URL % (',type', 'interactions')
PTMS_URL = OMNIPATH_URL % ('', 'ptms')

URLS = {
    'interactions': INTERACTIONS_URL,
    'ptms': PTMS_URL,
}


def get_version() -> str:
    """
    Get the software version.
    """
    
    return VERSION
