"""
Hello World
@author: John Morrison
@url: 
"""

# Always prefer setuptools over distutils
import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-your-username",
    version="0.0.2",
    author="John Morrison",
    author_email="jjosephmorrison@gmail.com",
    description="Helper functions package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JohnMorrisonn/lambdata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)