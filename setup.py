from setuptools import setup, find_packages
import os

setup(
  name='patentparse',
  version='0.0.0',
  author="Jackie Murphy",
  author_email="jackie@jamur2.net",
  description="US Patent parsing library",
  packages=find_packages(),
  package_dir={'patentparse': 'patentparse'},
  include_package_data=True,
)
