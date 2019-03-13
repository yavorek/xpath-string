from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    version='0.2.1',
    name='xpath_string',
    description='Module which allows to make xpath operations over string which represent xpath',
    long_descritpion=long_description,
    long_description_content_type='text/markdown',
    author='Tomasz Jaworski',
    author_email='jaworski.tomasz.91@gmail.com',
    packages=find_packages(),
    url="https://github.com/yavorek/xpath_string",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
