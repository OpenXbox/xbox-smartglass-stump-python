#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="xbox-smartglass-stump",
    version="1.10.0",
    author="OpenXbox",
    description="Meta package - Stump extension (TV streaming/IR control)",
    long_description=open('README.rst').read(),
    license="GPL",
    keywords="xbox one smartglass stump tv streaming",
    url="https://github.com/OpenXbox/xbox-smartglass-core-python",
    zip_safe=False,
    classifiers=[
        "Development Status :: 7 - Inactive",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'xbox-smartglass-core',
    ],
    extras_require={
    },
    entry_points={
    }
)
