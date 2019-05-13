from setuptools import setup

with open("README.md","r") as fh:
	long_description = fh.read()

setup(
	name='ackleys',
	version='0.0.1',
	description ='Ackleys function Generator',
	py_modules = ["ackleys"],
	package_dir={'':'src'},
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	url="https://github.com/adhishagc/Ackley-Function",
	author="Adhisha Gammanpila",
	author_email="adhishagc@gmail.com",
)