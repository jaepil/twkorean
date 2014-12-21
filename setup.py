# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Jaepil Jeong

from __future__ import print_function

import os

from setuptools import setup

try:
    from urllib import urlretrieve
except:
    from urllib.request import urlretrieve


__VERSION__ = "0.1.0"

_JAVA_LIB_URLS = [
    "https://repo1.maven.org/maven2/org/scala-lang/scala-library/2.11.4/scala-library-2.11.4.jar",
    "https://repo1.maven.org/maven2/org/apache/thrift/libthrift/0.9.2/libthrift-0.9.2.jar",
    "https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.14/snakeyaml-1.14.jar",
    "https://repo1.maven.org/maven2/com/twitter/twitter-text/1.10.2/twitter-text-1.10.2.jar",
    "https://repo1.maven.org/maven2/com/twitter/penguin/korean-text/2.3.3/korean-text-2.3.3.jar",
]
_PATH_TO_LIB = os.path.join(os.path.abspath(os.path.dirname((__file__))), "twkorean/data/lib")


def download_jars(target_path):
    for url in _JAVA_LIB_URLS:
        jar_name = os.path.basename(url)
        jar_path = os.path.join(target_path, jar_name)
        if not os.path.exists(jar_path):
            print("Downloading java package:", jar_name)
            urlretrieve(url, jar_path)


download_jars(target_path=_PATH_TO_LIB)


setup(
    name="twkorean",
    license="Apache 2.0",
    version=__VERSION__,
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
    download_url="https://github.com/jaepil/twkorean/tree/master",
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
