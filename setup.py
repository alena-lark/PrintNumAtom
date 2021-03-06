from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="printnum",
    version="0.1.9",
    author="alena-lark",
    author_email="AllyLarck@yandex.com",
    description="Printing a number of atoms in a molecule",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alena-lark/PrintNumAtom",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requares=['numpy', 'rdkit'],
    python_requires='>=3.7'
    )
