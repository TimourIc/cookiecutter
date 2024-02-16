from setuptools import find_packages
from setuptools import setup

packages=[
"numpy",
"pyyaml"
]

setup(name="{{cookiecutter.directory_name}}",
      version="0.0",
      dscription="{{cookiecutter.project_description}}",
      packages=find_packages(),
      install_requires=packages      
)
