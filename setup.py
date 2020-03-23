from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="ackley",
    version="1.1.0.0",
    description="A Python package to generate Ackley Function values.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/adhishagc/Ackley-Function",
    author="Adhisha Gammanpila",
    author_email="adhishagc@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    #include_package_data=True,
    install_requires=["numpy", "matplotlib"],
    packages=['ackley'],    
)