# setup.py

from setuptools import setup, find_packages

setup(
    name='image_scraper',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'selenium',
    ]
)
