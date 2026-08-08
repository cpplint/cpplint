#####################################
cpplint - static code checker for C++
#####################################

.. image:: https://img.shields.io/pypi/v/cpplint.svg
    :target: https://pypi.python.org/pypi/cpplint

.. image:: https://img.shields.io/pypi/pyversions/cpplint.svg
    :target: https://pypi.python.org/pypi/cpplint

.. image:: https://img.shields.io/pypi/status/cpplint.svg
    :target: https://pypi.python.org/pypi/cpplint

.. image:: https://img.shields.io/pypi/l/cpplint.svg
    :target: https://pypi.python.org/pypi/cpplint

.. image:: https://img.shields.io/pypi/dd/cpplint.svg
    :target: https://pypi.python.org/pypi/cpplint

.. image:: https://img.shields.io/pypi/dw/cpplint.svg
    :target: https://pypi.python.org/pypi/cpplint

.. image:: https://img.shields.io/pypi/dm/cpplint.svg
    :target: https://pypi.python.org/pypi/cpplint

Cpplint is a command-line tool to check C/C++ files for style issues according to `Google's C++ style guide <http://google.github.io/styleguide/cppguide.html>`_.

Cpplint used to be developed and maintained by Google Inc. at `google/styleguide <https://github.com/google/styleguide>`_. Nowadays, `Google is no longer maintaining the public version of cpplint <https://github.com/google/styleguide/pull/528#issuecomment-592315430>`_, and pretty much everything in their repo's PRs and issues about cpplint have gone unimplemented.

This fork aims to update cpplint to modern specifications, and be (somewhat) more open to adding fixes and features to make cpplint usable in wider contexts.


Installation
============

Use your preferred tool to install the ``cpplint`` package from PyPI. To install cpplint as a `uv <https://docs.astral.sh/uv>`_ tool, run:

.. code-block:: bash

    $ uv tool install cpplint

cpplint can also be run as a pre-commit hook by adding this to `.pre-commit-config.yaml`:

.. code-block:: yaml

  - repo: https://github.com/cpplint/cpplint
    rev:  # cpplint version number or git tag
    hooks:
      - id: cpplint
        args:
          - --filter=-whitespace/line_length,-whitespace/parens

cpplint also ships out of the box in `MegaLinter <https://megalinter.io/>`_, an open-source linter aggregator for CI (see its `cpplint documentation <https://megalinter.io/latest/descriptors/c_cpplint/>`_).

Usage
-----
.. code-block:: bash

    $ cpplint [OPTIONS] files

For full usage instructions, run:

.. code-block:: bash

    $ cpplint --help

Changes
=======

* Python 3 compatibility
* More default file extensions
* Continuous integration on GitHub
* Excluding files via ``--exclude``
* Customizable file extensions via ``--extensions``
* Recursive file discovery via ``--recursive``
* Skip entire blocks of code via ``// NOLINTBEGIN`` and ``// NOLINTEND``
* Support for more modern C++ features
* Support ``#pragma once`` as an alternative to header include guards
* ... and `quite a bit <https://github.com/cpplint/cpplint/blob/develop/CHANGELOG.rst>`_ more

Acknowledgements
================

Thanks to Google Inc. for open-sourcing their in-house tool.

Thanks to `our contributors <https://github.com/cpplint/cpplint/graphs/contributors>`_.

Maintainers
-----------

* `@aaronliu0130 <https://github.com/aaronliu0130>`_
* `@cclauss <https://github.com/cclauss>`_
* `@jayvdb <https://github.com/jayvdb>`_

Former
^^^^^^

* `@tkruse <https://github.com/tkruse>`_
* `@mattyclarkson <https://github.com/mattyclarkson>`_
* `@theandrewdavis <https://github.com/theandrewdavis>`_
