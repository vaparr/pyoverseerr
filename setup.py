from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyoverseerr",
    version="0.1.19",
    url="https://github.com/vaparr/pyoverseerr",
    author="Vaparr",
    author_email="Vaparr@vaparr.org",
    description="A python module to retrieve information from Overseerr.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["pyoverseerr"],
    package_dir={"": "pyoverseerr"},
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
