******************
Contributing guide
******************

Thanks for your interest in contributing to cpplint.

Any kinds of contributions are welcome: Bug reports, Documentation, Patches. However, here are some contributions you probably shouldn't make:

* Drastic reorganization
  * Making the code conform to Google's Python style guidelines
* Features that could be regarded as a security vulnerability

If you need some ideas, you may check out some of the tasks in our `issue tracker <https://github.com/cpplint/cpplint/issues>`_.

Development
===========

For many tasks, it is okay to just develop using a single installed python version. But if you need to test/debug the project in multiple python versions, you need to install those versions:

1. (Optional) Install multiple python versions

   1. (Optional) Install `pyenv <https://github.com/pyenv/pyenv-installer>`_ to manage python versions
   2. (Optional) Using pyenv, install the python versions used in testing::

        pyenv install 2.7.16
        pyenv install 3.6.8
        # ...
        pyenv local 2.7.16 3.6.8 ...

It may be okay to run and test python against locally installed libraries, but if you need to have a consistent build, it is recommended to manage your environment using virtualenv: `virtualenv <https://virtualenv.pypa.io/en/latest/>`_, `virtualenvwrapper <https://pypi.org/project/virtualenvwrapper/>`_::

    mkvirtualenv cpplint [-p /usr/bin/python3]
    pip install .[dev]

Alternatively, you can locally install patches like this::

    pip install -e .[dev]
    # for usage without virtualenv, add --user

Pull requests
-------------

When you're finished with a pull request, please:

* add a relevant test case to cpplint_unittest.py
* add a summary of what your changes do to CHANGELOG.rst
* specify the problem solved in the pull request
* make sure that your code passes the tests and lints
* don't force-push to the branch. These make the commit history messy, and we squash all commits when merging anyways.

.. _testing:

Testing
-------

You can test your changes under your local python environment by running the tests and lints below:

.. code-block:: bash

    # install test requirements
    pip install .[test]
    # run a single test
    pytest --no-cov cpplint_unittest.py -k testName
    # run a single CLI integration test
    pytest --no-cov cpplint_clitest.py -k testSillySample
    # run all tests. you don't have to run the above tests separately
    pytest
    # lint the code
    pylint cpplint.py
    flake8

Alternatively, you can run `tox` to automatically run all tests and lints. Use `-e ` followed by the python runner and version (which you must have installed) to automatically generate the testing environment and run the above tests and lints in it. For example, `tox -e py39` does the steps in Python 3.9, `tox -e py312` does the steps in Python 3.12, and `tox -e pypy3` does the steps using the latest version of the pypy interpreter.

Releasing
=========

The release process first prepares the documentation, then publishes to testpypi to verify, then releases to real pypi. Testpypi acts like real pypi, so broken releases cannot be deleted. For a typical bugfixing release, no special issue on testpypi is expected (but it's still good practice). The commands are documented below, and assume you've went through the testing steps above.

.. code-block:: bash

    # prepare files for release
    $EDITOR cpplint.py # increment the version
    $EDITOR CHANGELOG.rst # log changes
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

After releasing, it is be good practice to comment on completed GitHub issues to notify authors.

Catching up with Upstream
=========================

For maintainers, it is a regular duty to look at what cpplint changes were merged upstream and include them in this fork (though these updates happen rarely).

Checkout here and upstream google:

.. code-block:: bash

    git clone git@github.com:cpplint/cpplint.git
    cd cpplint
    git remote add google https://github.com/google/styleguide

To incorporate google's changes:

.. code-block:: bash

    git fetch google gh-pages

    ## Merge workflow (clean, no new commits)
    git checkout master -b updates
    git merge google/gh-pages # this will have a lot of conflicts
    # ... solve conflicts
    git merge -- continue
    
    ## Rebase workflow (dirty, creates new commits)
    git checkout -b updates FETCH_HEAD
    git rebase master # this will have a lot of conflicts, most of which can be solved with the next command (run repeatedly)
    # solve conflicts with files deleted in our fork (this is idempotent and safe to be called. when cpplint.py has conflicts, it will do nothing)
    git status | grep 'new file:' | awk '{print $3}' | xargs -r git rm --cached ; git status | grep 'deleted by us' | awk '{print $4}' | xargs -r git rm
    git status --untracked-files=no | grep 'nothing to commit' && git rebase --skip

    git push -u origin updates
    # check github action
    git push origin --delete updates

    git rebase updates master
    git branch -D updates
    git push

Setup fetching of pull requests in .git/config:

.. code-block:: bash

    [remote "origin"]
    	url = git@github.com:cpplint/cpplint.git
    	fetch = +refs/heads/*:refs/remotes/origin/*
    # following line should be new, fetches PRs from cpplint
    	fetch = +refs/pull/*/head:refs/remotes/origin/pr/*
    [remote "google"]
    	url = https://github.com/google/styleguide
    	fetch = +refs/heads/*:refs/remotes/google/*
    # following line should be new, fetches PRs from google/styleguides
    	fetch = +refs/pull/*/head:refs/remotes/google/pr/*


To compare this for with upstream (after git fetch):

.. code-block:: bash

    git diff google/gh-pages:cpplint/cpplint.py master:cpplint.py
    git diff google/gh-pages:cpplint/cpplint_unittest.py master:cpplint_unittest.py
