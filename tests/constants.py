# -*- coding: utf-8 -*-

"""Test constants for Bio2BEL OmniPath."""

import logging
import os

__all__ = [
    'HERE',
]

logger = logging.getLogger(__name__)

HERE = os.path.dirname(os.path.realpath(__file__))
