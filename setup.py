from setuptools import setup, find_packages

version = '0.1.2dev'

with open('requirements.txt') as requirements:
    install_requires = requirements.read().split()

setup(
    name="example-pkg-ccfiel",  # Replace with your own username
    version=version,
    author="Chris Ian Fiel",
    author_email="ccfiel@bai.ph",
    description="Python package for Paymongo API",
    long_description="A lightweight Python client for Paymongo API https://github.com/bailabs/paymongo",
    long_description_content_type="text/markdown",
    url="https://github.com/bailabs/paymongo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=install_requires
)

