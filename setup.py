from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


setup(
    name="touying",
    version="0.11.1",
    description="Export presentation slides in various formats for Touying",
    long_description_content_type="text/markdown",
    long_description=open(path.join(here, "README.md"), encoding="utf-8").read(),
    # The project's main homepage.
    url="https://github.com/touying-typ/touying-exporter",
    # Author details
    author="OrangeX4",
    author_email="318483724@qq.com",
    # Choose your license
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(exclude=("tests")),
    py_modules=["touying"],
    install_requires=["typst>=0.11.1", "python-pptx>=0.6", "pillow"],
)
