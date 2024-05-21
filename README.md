# Masquerade

![](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white)
![](https://img.shields.io/badge/Ruff-D7FF64.svg?style=flat&logo=Ruff&logoColor=black)
![GitHub last commit](https://img.shields.io/github/last-commit/essteer/masquerade?color=green)

A tool to generate random user-agent and referer data for GET requests.

## Contents

- [Installation](#installation)
  - [PyPI package](#pypi-package)
  - [GitHub repo](#github-repo)
- [Operation](#operation)
  - [Examples](#examples)
- [Local development](#local-development)
  - [Updates](#updates)
  - [Testing](#testing)

## Installation

To get hold of `masquerade` either install the package into your virtual environment from PyPI, or clone the GitHub repo for the full code base.

### PyPI package

Install the `masquerade` package from PyPI to retrieve just the tool with no extras.

Activate your existing project's virtual environment, then download `masquerade` using a package manager. The below example uses [Astral's](https://astral.sh/blog/uv) `uv`; substitute `pip` by dropping "`uv`" or use another package manager as needed: 

```console
$ uv pip install masquerade
```

### GitHub repo

Clone the `masquerade` repo from GitHub for the full source code. The repo includes the JSON source files used to generate the header data, a script to sync the programme if updates are made to the JSON files, and a test suite.

```console
$ git clone git@github.com:essteer/masquerade
```

The functional code within the package `src` directory has no dependencies beyond Python built-in modules. If you intend to make changes to your cloned version of the repo, you may optionally install the `project.optional-dependencies` declared in the `pyproject.toml` file.

First create and activate a virtual environment — the below example uses [Astral's](https://astral.sh/blog/uv) `uv`; substitute `pip` or use another package manager as needed — then install the `dev` dependencies:

![](https://img.shields.io/badge/Linux-FCC624.svg?style=flat&logo=Linux&logoColor=black)
![](https://img.shields.io/badge/macOS-000000.svg?style=flat&logo=Apple&logoColor=white)

```console
$ uv venv
$ source .venv/bin/activate
$ uv pip install hatchling==1.24.2 pre-commit==3.7.1 ruff==0.4.4
```

![](https://img.shields.io/badge/Windows-0078D4.svg?style=flat&logo=Windows&logoColor=white)

```console
$ uv venv
$ .venv\Scripts\activate
$ uv pip install hatchling==1.24.2 pre-commit==3.7.1 ruff==0.4.4
```

## Operation

Coming soon!

### Examples

Coming soon!

## Local development

Coming soon!

### Updates

Coming soon!

### Testing

`masquerade` uses Python's in-built `unittest` module. 

To run the entire test suite using `discover`, or specify an individual test file from the `tests` directory — for example `test_assets.py` — run one of the following shell commands from the project `root` directory:

![](https://img.shields.io/badge/Linux-FCC624.svg?style=flat&logo=Linux&logoColor=black)
![](https://img.shields.io/badge/macOS-000000.svg?style=flat&logo=Apple&logoColor=white)

```console
$ python3 -m unittest discover  # run all tests
$ python3 -m unittest tests.test_assets  # test a single file
```

![](https://img.shields.io/badge/Windows-0078D4.svg?style=flat&logo=Windows&logoColor=white)

```console
$ python -m unittest discover  # run all tests
$ python -m unittest tests.test_assets  # test a single file
```
