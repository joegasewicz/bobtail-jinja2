
from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="bobtail-jinja2",
    version="0.0.2",
    description="Use Jinja2 templating engine with Bobtail",
    packages=["bobtail_jinja2"],
    py_modules=["bobtail_jinja2"],
    install_requires=[
        "bobtail",
        "jinja2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joegasewicz/bobtail-jinja2",
    author="Joe Gasewicz",
    author_email="joegasewicz@gmail.com"
)