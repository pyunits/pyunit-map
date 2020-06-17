#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/5/9 11:50
# @Author: Jtyoui@qq.com
import os
from setuptools import setup, find_packages
from distutils.extension import Extension
from os.path import join


dirs = os.path.abspath(os.path.dirname(__file__))

with open(dirs + os.sep + 'README.md', encoding='utf-8') as f:
    long_text = f.read()

ext_modules = [
    Extension('randomak', [join(dirs, 'randomak.c')])
]

setup(
    name='pyunit_map',
    version='2020.6.17',
    description='地图API接口',
    long_description=long_text,
    long_description_content_type="text/markdown",
    url='https://github.com/PyUnit/pyunit-map',
    author='Jtyoui',
    author_email='jtyoui@qq.com',
    license='MIT Licence',
    packages=find_packages(),
    platforms='any',
    package_data={'pyunit_map': ['*.py', '*.c']},
    install_requires=[],
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
