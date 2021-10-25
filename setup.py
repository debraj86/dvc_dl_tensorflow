from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="debraj86",
    description="A small package for dvc dl pipeline tensorflow demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/debraj86/dvc_dl_tensorflow",
    author_email="debraj86ghosh@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'tensorflow',
        'numpy',
        'matplotlib',
        'tqdm',
        'PyYAML',
        'boto3' #for aws 
        ]
)

