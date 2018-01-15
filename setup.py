# coding: utf-8

from setuptools import setup, find_packages


NAME = "sci_comp"
VERSION = "0.1.0"
DESCRIPTION = "Sample package for Python-Guide.org"
AUTHOR = "Kantouzin"
AUTHOR_EMAIL = "kantouzin0113@gmail.com"
URL = "https://github.com/Kantouzin/sci_comp"

REQUIRES = ["numpy"]

with open('README.rst') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    install_requires=REQUIRES,
    url=URL,
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
