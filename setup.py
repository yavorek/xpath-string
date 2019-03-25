from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    version='0.2.2',
    name='xpath_string',
    description='Module which allows to make xpath operations over string which represent xpath',
    long_description=readme,
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
