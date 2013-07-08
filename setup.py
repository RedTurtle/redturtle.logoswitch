# -*- coding: utf-8 -*-
"""
This module contains the tool of redturtle.logoswitch
"""
import os
from setuptools import setup, find_packages

version = '1.1.0'

tests_require = ['plone.app.testing']

setup(name='redturtle.logoswitch',
      version=version,
      description="Allows users to change plone portal logo from a given images list",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 3.3",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='http://svn.plone.org/svn/plone/products/redturtle.logoswitch',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['redturtle', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        ],
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
