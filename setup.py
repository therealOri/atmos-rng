import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="atmos-rng",
    version="1.0.0",
    author="therealOri",
    license="GPL-3.0",
    install_requires=[
        "requests",
    ],
    author_email="therealOri@duck.com",
    description="A simple random generator based off of atmospheric noise instead of math.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/therealOri/atmos-rng",
)
