from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='currency-converter-cli',
    version='1.0.0',
    author='Abdel Rahman Rottab',
    author_email='abdurrahman.rottab@gmail.com',
    description='Python package for currency convertion',
    long_description=long_description,
    requires=[
        'pony',
    ],
    python_requires='>=3.6',
    packages=[
        'currency_converter_cli'
    ],
    entry_points={
        'console_scripts': [
            'cc = currency_converter_cli.__main__:main',
            'currency-converter = currency_converter_cli.__main__:main'
        ]
    })
