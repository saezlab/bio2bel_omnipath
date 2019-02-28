# -*- coding: utf-8 -*-

"""Constants for Bio2BEL OmniPath."""

from bio2bel import get_data_dir

__all__ = [
    'VERSION',
    'MODULE_NAME',
    'DATA_DIR',
    'get_version',
]

VERSION = '0.0.1'
MODULE_NAME = 'omnipath'
DATA_DIR = get_data_dir(MODULE_NAME)

PROTEIN_NAMESPACE = 'UNIPROT'

OMNIPATH_URL = 'http://omnipathdb.org/'
INTERACTIONS_URL = '%s/interactions/' % OMNIPATH_URL
PTMS_URL = '%s/ptms/' % OMNIPATH_URL
INTERACTIONS_PATH = os.path.join(DATA_DIR, 'interactions.tsv')
PTMS_PATH = os.path.join(DATA_DIR, 'ptms.tsv')

def get_version() -> str:
    """Get the software version."""
    return VERSION
