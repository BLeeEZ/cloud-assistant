import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cloud_assistant",
    version="0.0.1",
    author="Maximilian Bauer",
    author_email="bauer.maximilian@web.de",
    description="Cloud assistant for cli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bleeez/cloud-assistant",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)