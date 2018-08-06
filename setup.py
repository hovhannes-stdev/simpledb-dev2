##################################################
# Copyright (C) 2017, All rights reserved.
##################################################

import os
import re

from setuptools import find_packages, setup

def _read_properties():
    init_path = os.path.abspath(os.path.join("simpledbdev2", "__init__.py"))
    regex = re.compile("^\\s*__(?P<key>.*)__\\s*=\\s*\"(?P<value>.*)\"\\s*$")
    with open(init_path, "rt") as f:
        props = {}
        for line in f.readlines():
            m = regex.match(line)
            if m is not None:
                props[m.group("key")] = m.group("value")

    return props

props = _read_properties()
version = props["version"]
description = props["description"]

setup(
    name="simpledb-dev3",
    version=version,
    description=description,
    setup_requires=["setuptools-markdown"],
    long_description_markdown_filename="README.md",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.6",
    ],
    url="https://github.com/hovhannes-stdev/simpledb-dev2",
    author="Matthew Painter and others",
    author_email="hovhannes@stdevmail.com",
    license="GNU GPL v3",
    packages=find_packages(),
    install_requires=[
        "pyprelude",
        "web.py==0.40-dev1"
    ],
    entry_points={
        "console_scripts": [
            "simpledb-dev3 = simpledbdev2.__main__:_main"
        ]
    },
    include_package_data=True,
    package_data={ "simpledbdev2.templates": ["*.xml"] },
    test_suite="simpledbdev2.tests.suite",
    zip_safe=False)
