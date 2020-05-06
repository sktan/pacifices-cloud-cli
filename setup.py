"""
Copyright 2020 Steven Tan

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import setuptools

with open("README.md") as fp:
  LONG_DESCRIPTION = fp.read()

setuptools.setup(
  name="pacifices-cloud",
  version="0.1.0",

  description="A CLI tool for managing your https://pacifices.cloud servers",
  long_description=LONG_DESCRIPTION,
  long_description_content_type="text/markdown",
  keywords='pacifices cloud pacifices.cloud',

  author="Steven Tan",
  author_email="git@sktan.com",
  url="https://github.com/sktan/pacifices-cloud-cli",

  packages=setuptools.find_packages(),
  py_modules=['pacificescloud'],

  install_requires=[
    requirement.strip() for requirement in open('requirements.txt').readlines()
  ],

  entry_points={
    'console_scripts': [
      'pacifices-cloud=pacificescloud:main',
    ]
  },

  python_requires=">=3.6",

  classifiers=[
    "Development Status :: 4 - Beta",

    "Environment :: Console",
    "Operating System :: OS Independent",

    "License :: OSI Approved :: MIT License",

    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",

    "Topic :: Utilities",

    "Typing :: Typed",
  ],
)
