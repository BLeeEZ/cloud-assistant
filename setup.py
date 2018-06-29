import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

import subprocess
import re
__version__ = subprocess.check_output(["git", "describe", "--tags"]).rstrip()
__version__ = __version__.decode('UTF-8')
__version__ = re.search("(\d+\.\d+\.\d+)(?:(\-\d+))?", __version__).group(0)

setuptools.setup(
    name="cloudassist",
    version=__version__,
    author="Maximilian Bauer",
    author_email="bauer.maximilian@web.de",
    description="Cloud assistant for cli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bleeez/cloud-assistant",
    install_requires=['configparser', 'caldav'],
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["cloudassist=cloudassist.__main__:main"]},
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
