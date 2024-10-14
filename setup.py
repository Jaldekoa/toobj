from setuptools import setup
from pathlib import Path

VERSION = "0.0.1"
THIS_PATH = Path(__file__).parent
DESCRIPTION = "Python package that transforms flat or nested dictionaries into objects."
LONG_DESCRIPTION = (THIS_PATH / "README.md").read_text(encoding="utf-8")


setup(
    name="toobj",
    version=VERSION,
    url="https://github.com/Jaldekoa/toobj",
    author="Jon Aldekoa",
    author_email="jaldekoa@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=["toobj"],
    test_suite='toobj.tests',
    platforms=["Any"],
    install_requires=["setuptools", "pytest"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ]
)