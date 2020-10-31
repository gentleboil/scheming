import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tscheme-gentleboil"
    version="0.0.1",
    author="Tony Simmers",
    author_email="simmers.tony@gmail.com",
    description="A simple harness to validate JSON against a schema",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gentleboil/scheming.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)