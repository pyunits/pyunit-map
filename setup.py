#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/5/9 11:50
# @Author: Jtyoui@qq.com
from setuptools import setup, find_packages
from pyunit_map import __version__, __author__, __description__, __email__, __names__, __url__
from distutils.extension import Extension
from os.path import join
import os

dirs = os.path.abspath(os.path.dirname(__file__))

with open(dirs + os.sep + 'README.md', encoding='utf-8') as f:
    long_text = f.read()

ext_modules = [
    Extension('randomak', [join(dirs, 'randomak.c')])
]

setup(
    name=__names__,
    version=__version__,
    description=__description__,
    long_description=long_text,
    long_description_content_type="text/markdown",
    url=__url__,
    author=__author__,
    author_email=__email__,
    license='MIT Licence',
    packages=find_packages(),
    platforms='any',
    package_data={__names__: ['*.py', '*.c']},
    install_requires=['openpyxl==3.0.3', 'pandas==1.0.1', 'requests==2.22.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux"
    ],
    zip_safe=False,
    ext_modules=ext_modules
)
