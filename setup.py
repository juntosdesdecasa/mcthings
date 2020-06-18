#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import codecs
import os
import re
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
readme_md = os.path.join(here, 'README.md')

version_py = os.path.join(here, 'mcthings', '_version.py')
with codecs.open(version_py, 'r', encoding='utf-8') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

# Get the package description from the README.md file
with codecs.open(readme_md, encoding='utf-8') as f:
    long_description = f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mcthings',
    version=version,
    packages=['mcthings', 'mcthings.core', 'mcthings.decorators'],
    include_package_data=True,
    license='ASL',
    description='McThings is a python library for building things in Minecraft',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/juntosdesdecasa/mcthings',
    author='Alvaro del Castillo',
    author_email='alvaro.delcastillo@gmail.com',
    keywords="development library minecraft buildings games",
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development'
    ],
    install_requires=[
        'mcpi',
        'minecraftstuff',
        'nbt'
    ],
    python_requires='>=3.4'
)
