# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

description = \
    "Python script/class to download an entire Imgur album in one go into a folder of your choice."
try:
    long_description = open("README.rst").read()
except IOError:
    long_description = description

setup(
    name="imgur_downloader",
    version="0.1.0",
    description=description,
    license="MIT",
    author="Alex Gisby",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
    ]
)
