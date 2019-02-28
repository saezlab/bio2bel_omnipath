# -*- coding: utf-8 -*-

"""Parsers and downloaders for Bio2BEL OmniPath."""

import os
import log
import hashlib

import bio2bel.downloading
import urllib.request
import pandas as pd


from .constants import URLS, DATA_DIR


log = logging.getLogger(__name__)


def download(url, force_download = False):
    """
    Downloads anything and manages cache.
    """
    
    local_path = os.path.join(
        DATA_DIR,
        hashlib.md5(url.encode('utf-8')).hexdigest(),
    )
    
    if not os.path.exists(local_path) or force_download:
        
        log.info('downloading %s to %s', url, local_path)
        urllib.request.urlretrieve(url, local_path)
        
    else:
        
        log.info('using cached data at %s', local_path)
    
    return local_path


def get(query_type, url = None, cache = True, force_download = False):
    """
    Retrieves a data frame with OmniPath data.
    
    :param str query_type:
        The web service query type to use. At the moment `interactions`
        or `ptms` available.
    :param str url:
        Path or URL to the input data. If None default URL used from
        :py:mod:``constants``.
    :param bool cache:
        Save local copy of the input file or only load to data frame.
    :param bool force_download:
        Download again even if local copy exists.
    """
    
    if url is None:
        
        try:
            
            url = URLS[query_type]
            
        except KeyError:
            
            raise NotImplementedError
    
    if (not os.path.exists(url) or force_download) and cache:
        
        url = download(url, force_download = force_download)
    
    df = pd.read_table(url)
    
    return df


def get_interactions(**kwargs):
    
    return get('interactions', **kwargs)


def get_ptms(**kwargs):
    
    return get('ptms', **kwargs)


def get_complexes(**kwargs):
    
    return get('complexes', **kwargs)


def get_annotations(**kwargs):
    
    return get('annotations', **kwargs)
