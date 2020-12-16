from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fp:
    install_requires = fp.read()

setup(
    name="twinfield",
    version="0.0.1",
    author="Melvin Folkers",
    author_email="melvin@zypp.io",
    description="Read data from Twinfield through API with SOAP messages and write to Azure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="python, twinfield, azure, API",
    url="https://github.com/zypp-io/twinfield",
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={"console_scripts": ["run=df_to_azure.export:run"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    project_urls={
        "Bug Reports": "https://github.com/zypp-io/twinfield/issues",
        "Source": "https://github.com/zypp-io/twinfield",
    },
)