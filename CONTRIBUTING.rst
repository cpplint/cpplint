******************
Contributing guide
******************

Thanks for your interest in contributing to cpplint.

Any kinds of contributions are welcome: Bug reports, Documentation, Patches. However, here are some contributions you probably shouldn't make:

* Drastic reorganization
   * Making the code conform to Google's Python style guidelines
* Features that could be regarded as a security vulnerability
* Very imperformant code covering very rare cases

If you need some ideas, you may check out some of the tasks in our `issue tracker <https://github.com/cpplint/cpplint/issues>`_.

We encourage uncontroversial refactoring code that your PR touches, such as adding type hints and converting to match-case statements, as long as it is reasonably confined to the lines your PR touches. Any TODO items added should include your username and brief reasoning (e.g. ``@todo(aaronliu0130): should use walrus``).

Development
===========

For many tasks, it is okay to just develop using a single installed python version. But if you need to test/debug the project in multiple python versions, you need to install those versions:

1. (Optional) Install multiple python versions

   1. (Optional) Install `pyenv <https://github.com/pyenv/pyenv-installer>`_ to manage python versions
   2. (Optional) Using pyenv, install the python versions used in testing::

        pyenv install 3.<version>
        # ...
        pyenv local 3.<version> ...

It may be okay to run and test python against locally installed libraries, but if you need to have a consistent build, it is recommended to manage your environment using virtualenv: `virtualenv <https://virtualenv.pypa.io/en/latest/>`_, `virtualenvwrapper <https://pypi.org/project/virtualenvwrapper/>`_::

    mkvirtualenv cpplint [-p /usr/bin/python3]
    pip install .[dev]

Alternatively, you can locally install patches like this::

    pip install -e .[dev]
    # for usage without virtualenv, add --user

Please install pre-commit locally to run the linters before committing::

    pipx install pre-commit
    pre-commit install

Pull requests
-------------

When you're finished with a pull request, please:

* add a relevant test case to cpplint_unittest.py
* add a summary of what your changes do under changes/; see below
* specify the problem solved in the pull request
* make sure that your code passes the tests and lints
* don't force-push to the branch just to squash everything into a single commit. These make the commit history messy, and we'll squash it when merging anyways.
* name the pull request as a `Conventional Commit <https://www.conventionalcommits.org>`_

To avoid conflicts, changelog entries should be added as new files under changes/, which we'll use towncrier to concatenate when releasing.
Each file should be named in the format of "{issue number}.{change type}", (e.g. where {change type} is one of the following:

* ``breaking``, for breaking changes, such as removal of
* ``feature``, for changes that add a feature, such as support for new syntax or new checks
* ``bugfix``, for changes that correct wrong behavior, such as false positives on specific syntax
* ``refactor``, for significant code changes, such as great performance optimizations (probably not just extracting code into functions)
* Changes that don't affect code do not need a changelog entry.

Every entry should be one line like the entries in CHANGELOG.rst. Note that the changelog is `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_, meaning, among other things, that inline code needs two backticks instead of one.

If you believe a change is not significant enough for a changelog entry, please mention this in the PR description.

.. _testing:

Testing
-------

You can test your changes under your local python environment by running the tests and lints below:

.. code-block:: bash

    # install dev requirements
    pip install .[dev]
    # run a single test
    pytest --no-cov cpplint_unittest.py -k testName
    # run a single CLI integration test
    pytest --no-cov cpplint_clitest.py -k testSillySample
    # run all tests. you don't have to run the above tests separately
    pytest
    # lint the code
    pylint cpplint.py
    pre-commit run --all-files

Alternatively, you can run ``tox`` to automatically run all tests and lints. Use ``-e `` followed by the python runner and version (which you must have installed) to automatically generate the testing environment and run the above tests and lints in it. For example, `tox -e py39` does the steps in Python 3.9, `tox -e py313` does the steps in Python 3.13, and `tox -e pypy3` does the steps using the latest version of the pypy interpreter.

Releasing
=========

The release process first prepares the documentation, then publishes to testpypi to verify, then releases to real pypi. The following instructions assume you have already run the testing steps above.

Have towncrier and twine installed. They are not included in ``.[dev]`` as release tools are not necessary for regular development and testing.

To prepare the changelog, bump ``cpplint.__VERSION__`` so towncrier knows the version, run ``towncrier build``, prepend NEWS.rst to CHANGELOG.rst and delete the former, then match the output format:

* Changes should be ordered by importance in one, big list.
* Non-maintainer contributors should be credited.
* Linking pull requests is optional.

Testpypi acts like real pypi, so broken releases cannot be deleted. For a typical bugfixing release, no special issue on testpypi is expected (but it's still good practice).

Commands that can do the above:

.. code-block:: sh

    # prepare files for release
    $EDITOR cpplint.py # increment the version
    towncrier build --yes # creates NEWS.rst
    cat CHANGELOG.rst >> NEWS.rst && git mv -f NEWS.rst CHANGELOG.rst # prepend towncrier output to changelog
    $EDITOR CHANGELOG.rst # adjust
    git add cpplint.py CHANGELOG.rst
    git commit -m "Releasing x.y.z"
    # Build
    pip install --upgrade build wheel twine
    rm -rf dist
    python -m build --sdist --wheel
    # Test release, requires account on testpypi
    twine upload --repository testpypi dist/*
    # ... Check website and downloads from https://test.pypi.org/project/cpplint/
    # Actual release
    twine upload dist/*
    git tag x.y.z
    git push --tags

After releasing, it is good practice to comment on completed GitHub issues to notify authors.
