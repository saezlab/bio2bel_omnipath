# -*- coding: utf-8 -*-

"""Comprehensive database of literature curated signaling pathways"""

from .constants import get_version
from .manager import Manager

__all__ = [
    'Manager',
    'get_version',
]
