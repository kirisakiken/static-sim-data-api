from setuptools import setup, find_packages

setup(
    name="static-sim-data-api",
    version="0.1",
    author="Bezmican Zehir",
    packages=find_packages(),
    install_requires=[
        "fastapi ~= 0.100.0",
        "uvicorn ~= 0.23.1",
    ],
)