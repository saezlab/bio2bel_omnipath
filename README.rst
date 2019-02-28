Bio2BEL OmniPath |build|
==================================================
Comprehensive database of literature curated signaling pathways

Installation |pypi_version| |python_versions| |pypi_license|
------------------------------------------------------------
``bio2bel_omnipath`` can be installed easily from
`PyPI <https://pypi.python.org/pypi/bio2bel_omnipath>`_
with the following code in your favorite terminal:

.. code-block:: sh

    $ python3 -m pip install bio2bel_omnipath

or from the latest code on `GitHub <https://github.com/bio2bel/omnipath>`_ with:

.. code-block:: sh

    $ python3 -m pip install git+https://github.com/bio2bel/omnipath.git

Setup
-----
OmniPath can be downloaded and populated from either the
Python REPL or the automatically installed command line utility.

Python REPL
~~~~~~~~~~~
.. code-block:: python

    >>> import bio2bel_omnipath
    >>> omnipath_manager = bio2bel_omnipath.Manager()
    >>> omnipath_manager.populate()

Command Line Utility
~~~~~~~~~~~~~~~~~~~~
.. code-block:: sh

    bio2bel_omnipath populate


.. |build| image:: https://travis-ci.com/bio2bel/omnipath.svg?branch=master
    :target: https://travis-ci.com/bio2bel/omnipath
    :alt: Build Status

.. |documentation| image:: http://readthedocs.org/projects/bio2bel-omnipath/badge/?version=latest
    :target: http://bio2bel.readthedocs.io/projects/omnipath/en/latest/?badge=latest
    :alt: Documentation Status

.. |pypi_version| image:: https://img.shields.io/pypi/v/bio2bel_omnipath.svg
    :alt: Current version on PyPI

.. |coverage| image:: https://codecov.io/gh/bio2bel/omnipath/coverage.svg?branch=master
    :target: https://codecov.io/gh/bio2bel/omnipath?branch=master
    :alt: Coverage Status

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/bio2bel_omnipath.svg
    :alt: Stable Supported Python Versions

.. |pypi_license| image:: https://img.shields.io/pypi/l/bio2bel_omnipath.svg
    :alt: MIT License
