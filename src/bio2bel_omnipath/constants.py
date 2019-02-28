# -*- coding: utf-8 -*-

"""Constants for Bio2BEL OmniPath."""

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

PROTEIN_NAMESPACE = 'UNIPROT'

OMNIPATH_URL = 'http://omnipathdb.org/'
INTERACTIONS_URL = '%s/interactions/' % OMNIPATH_URL
PTMS_URL = '%s/ptms/' % OMNIPATH_URL

URLS = {
    'interactions': INTERACTIONS_URL,
    'ptms': PTMS_URL,
}


def get_version() -> str:
    """Get the software version."""
    return VERSION
