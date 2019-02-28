# -*- coding: utf-8 -*-

"""Manager for Bio2BEL OmniPath."""

from typing import Mapping

from bio2bel import AbstractManager
from .constants import MODULE_NAME
from .models import Base
import .parser

__all__ = [
    'Manager',
]

class Manager(AbstractManager):
    """Manages the Bio2BEL OmniPath database."""

    module_name = MODULE_NAME
    _base = Base

    def is_populated(self) -> bool:
        """Check if the Bio2BEL OmniPath database is populated."""
        raise NotImplementedError

    def summarize(self) -> Mapping[str, int]:
        """Summarize the contents of the Bio2BEL OmniPath database."""
        raise NotImplementedError

    def populate(self) -> None:
        """Populate the Bio2BEL OmniPath database."""
        raise NotImplementedError
