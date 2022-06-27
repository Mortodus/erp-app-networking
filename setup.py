from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in networking/__init__.py
from networking import __version__ as version

setup(
	name="networking",
	version=version,
	description="Huawei Provision",
	author="Henry Dobinson",
	author_email="henry.d@cloud-fibre.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
