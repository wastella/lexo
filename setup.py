from setuptools import setup, find_packages

setup(
    name="lexo",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'fsrs',
        'google-generativeai'
    ],
)
