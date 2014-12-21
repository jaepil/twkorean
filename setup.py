# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Jaepil Jeong

from distutils.core import setup


__version__ = "0.1.0"


setup(
    name="twkorean",
    license="Apache 2.0",
    version=__version__,
    packages=["twkorean"],
    package_dir={"twkorean": "twkorean"},
    package_data={
        "twkorean": [
            "data/lib/*.jar",
        ],
    },
    install_requires=[
        "JPype1"
    ],
    author="Jaepil Jeong",
    author_email="jaepil@{nospam}appspand.com",
    url="https://github.com/jaepil/twkorean/",
    classifiers=[
        "Programming Language :: Java",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    platforms=[
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows Vista",
        "Operating System :: POSIX :: Linux",
    ],
    keywords=[
        "twitter-korean-text",
        "morphological analyzer",
        "morphology", "analyzer"
        "korean", "tokenizer"
    ],
    description="Python interface to twitter-korean-text, a Korean morphological analyzer."
)
