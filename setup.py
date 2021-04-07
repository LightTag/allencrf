import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
REQUIREMENTS = (HERE / "requirements.txt").read_text().split("\n")
# This call to setup() does all the work
setup(
    name="allencrf",
    version="1.0.0",
    description="An PyTorch CRF implementation extracted from AllenNLP",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/lighttag/allencrf",
    author="Tal Perry / Joel Grus",
    author_email="tal@lighttag.io",
    license="Apache 2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["allencrf"],
    include_package_data=True,
    install_requires=REQUIREMENTS,
)
