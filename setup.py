# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# picasso is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Invenio digital library framework."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('picasso', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='picasso',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='picasso Invenio',
    license='MIT',
    author='CERN',
    author_email='info@picasso.com',
    url='https://github.com/picasso/picasso',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'picasso = invenio_app.cli:cli',
        ],
        'invenio_base.apps': [
            'picasso_records = picasso.records:picasso',
        ],
        'invenio_base.blueprints': [
            'picasso = picasso.theme.views:blueprint',
            'picasso_records = picasso.records.views:blueprint',
        ],
        'invenio_assets.webpack': [
            'picasso_theme = picasso.theme.webpack:theme',
        ],
        'invenio_config.module': [
            'picasso = picasso.config',
        ],
        'invenio_i18n.translations': [
            'messages = picasso',
        ],
        'invenio_base.api_apps': [
            'picasso = picasso.records:picasso',
         ],
        'invenio_jsonschemas.schemas': [
            'picasso = picasso.records.jsonschemas'
        ],
        'invenio_search.mappings': [
            'records = picasso.records.mappings'
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
