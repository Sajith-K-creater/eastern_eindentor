from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in eastern_eindentor/__init__.py
from eastern_eindentor import __version__ as version

setup(
	name="eastern_eindentor",
	version=version,
	description="Hierarchial indent approval system",
	author="ideenkreisetech pvt ltd",
	author_email="info@ideenkreisetech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
