from setuptools import find_packages, setup

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3 :: Only",
    "Natural Language :: English",
]

KEYWORDS = ["python", "strings", "string-analysis"]
DEPENDENCIES = []
VERSION = "0.1.2"
NAME = "pystrtools"
AUTHOR_NAME = "Magnus Zahle"
AUTHOR_EMAIL = "objectivesquid@outlook.com"
LICENSE = "MIT"
GITHUB_URL = "https://github.com/objectiveSquid/pystrtools"

SHORT_DESCRIPTION = "A library for doing many things - with strings, in Python."
with open("README.md", "r") as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(
    name=NAME,
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    packages=find_packages(),
    install_requires=DEPENDENCIES,
)
