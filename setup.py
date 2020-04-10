from setuptools import setup

version = '0.1.0dev'

with open('requirements.txt') as requirements:
    install_requires = requirements.read().split()

setup(
    name='paymongo',
    description="Paymongo Python Library",
    version=version,
    author='Chris Ian Fiel',
    author_email='ccfiel@bai.ph',
    packages=[
        'paymongo'
    ],
    install_requires=install_requires
)