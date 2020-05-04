""" Package Setup """
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
