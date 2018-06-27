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
    install_requires=['configparser', 'caldav'],
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["cassist=cloud_assistant.__main__:main"]},
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
