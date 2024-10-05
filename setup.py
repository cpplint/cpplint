#! /usr/bin/env python
from setuptools import setup
import cpplint

# some pip versions bark on comments
def read_without_comments(filename):
    with open(filename) as f:
        return [line for line in f.read().splitlines() if not len(line) == 0 and not line.startswith('#')]

test_required = read_without_comments('test-requirements')

setup(name='cpplint',
      version=cpplint.__VERSION__,
      py_modules=['cpplint'],
      # generate platform specific start script
      entry_points={
          'console_scripts': [
              'cpplint = cpplint:main'
          ]
      },
      install_requires=[],
      url='https://github.com/cpplint/cpplint',
      download_url='https://github.com/cpplint/cpplint',
      keywords=['lint', 'python', 'c++'],
      maintainer='cpplint Developers',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'Intended Audience :: End Users/Desktop',
                   'License :: Freely Distributable',
                   'License :: OSI Approved :: BSD License',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 3 :: Only',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   'Programming Language :: Python :: 3.10',
                   'Programming Language :: Python :: 3.11',
                   'Programming Language :: Python :: 3.12',
                   'Programming Language :: C++',
                   'Topic :: Software Development :: Quality Assurance'],
      description='Automated checker to ensure C++ files follow Google\'s style guide',
      long_description=open('README.rst').read(),
      license='BSD-3-Clause',
      tests_require=test_required,
      # extras_require allow pip install .[dev]
      extras_require={
          'test': test_required,
          'dev': read_without_comments('dev-requirements') + test_required
      })
