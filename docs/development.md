<h1 align="center" id="title">Masquer &mdash; development notes</h1>

<p align="center">
  <a href="https://github.com/essteer/masquer/actions/workflows/test.yaml"><img src="https://github.com/essteer/masquer/actions/workflows/test.yaml/badge.svg"></a>
  <a href="https://pypi.org/project/masquer/"><img src="https://img.shields.io/badge/PyPI-v1.2.2-3775A9.svg?style=flat&logo=PyPI&logoColor=white"></a>
  <a href="https://pypi.org/project/masquer/"><img src="https://img.shields.io/badge/Python-3.9_~_3.12-3776AB.svg?style=flat&logo=Python&logoColor=white"></a>
  <a href="https://snyk.io/test/github/essteer/masquer"><img src="https://snyk.io/test/github/essteer/masquer/badge.svg?name=Snyk&style=flat&logo=Snyk"></a>
</p>

<p align="center">
  <a href="https://astral.sh"><img src="https://img.shields.io/badge/Astral-261230.svg?style=flat&logo=Astral&labelColor=555&logoColor=white"></a>
  <a href="https://hub.docker.com/r/essteer/masquer"><img src="https://img.shields.io/badge/Docker-2496ED.svg?flat&logo=Docker&labelColor=555&logoColor=white"></a>
  <a href="https://github.com/tiangolo/fastapi"><img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=FastAPI&labelColor=555&logoColor=white"></a>
  <a href="https://github.com/pypa/hatch"><img src="https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg"></a>
  </p>

<p align="center">
A tool to generate random user-agent and referer data for HTTP requests.
</p>

## Development

The sections that follow provide notes for use in developing `masquer`.

See also the main [`README.md`](https://github.com/essteer/masquer/blob/main/README.md) and [`deployment`](https://github.com/essteer/masquer/blob/main/docs/deployment.md) notes.

- [Git repository](#git-repository)
- [Asset updates](#asset-updates)
- [Docker](#docker)
- [Formatting](#formatting)
- [GitHub Actions](#github-actions)
- [Logs](#logs)
- [Tests](#tests)

The following details will assist with making and testing changes to a cloned version of the repository.

## Git repository

[![](https://img.shields.io/badge/GitHub-masquer-181717.svg?flat&logo=GitHub&logoColor=white)](https://github.com/essteer/masquer)

Clone the `masquer` repo for the full source code:

```console
$ git clone git@github.com:essteer/masquer
```

Create a virtual environment and install the dependencies declared in the `[project.optional-dependencies]` and `[uv.tool]` sections of `pyproject.toml` &mdash; the command below assumes a version of `uv` above `0.4.0`:

```console
$ cd masquer
$ uv sync --all-extras
```

[<h3 align="center">:arrow_up:</h3>](#title)

## Asset updates

The `update.sh` shell script in the root directory updates the `header.json` and `referer.json` files in the `assets` directory to the latest versions, then uses this data to update the `assets.py` file used by the `masquer` package.

```console
$ chmod +x update.sh
$ ./update.sh
2024-09-17 14:34:03 - INFO - update.py:29 - Fetched user-agent data
2024-09-17 14:34:04 - INFO - update.py:74 - Fetched referer data
2024-09-17 14:34:04 - INFO - update.py:133 - Saved user-agent and referer JSON data to assets.py
2024-09-17 14:34:04 - INFO - update.sh - Asset update OK
```

In case of issues updating the assets, ensure all dependencies are installed and check the source URLs are available:

- User-agent data: [`https://www.useragents.me/`](https://www.useragents.me/)
- Referer data: [`https://gs.statcounter.com/search-engine-market-share/desktop/worldwide`](https://gs.statcounter.com/search-engine-market-share/desktop/worldwide)

If using custom JSON data, the `update_assets()` function inside `update.py` can still be used to sync changes with the `assets.py` file inside the `masquer` package.

[<h3 align="center">:arrow_up:</h3>](#title)

## Docker

TBC

### GitHub Action

A `docker.yaml` workflow is in place to build and publish a Docker image when a new release is made on the `main` branch &mdash; see the [`deployment`](https://github.com/essteer/masquer/blob/main/docs/deployment.md) notes for more details.

[<h3 align="center">:arrow_up:</h3>](#title)

## Formatting

 <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"></a>

Python files in `masquer` are formatted using Ruff.

### Pre-commit hook

A pre-commit hook is configured in `.pre-commit-config.yaml` to check and format files before they are committed locally. Scripts that fail the format check must be re-staged and then committed.

### GitHub Action

A GitHub action is configured in `.github/workflows/ruff.yaml` to run Ruff checks for any push or pull request to the `main` branch.

[<h3 align="center">:arrow_up:</h3>](#title)

## GitHub Actions

GitHub actions are configured in `.github/workflows` and are in place for all pushes and pull requests for the `main` branch:

- `ruff.yaml`: checks and formats Python code (see [Formatting](#formatting))
- `test.yaml`: runs unit tests on the code in a matrix pattern (see [Tests](#tests))

A `docker.yaml` workflow is in place to build and publish a Docker image when a new release is made on the `main` branch &mdash; see the [`deployment`](https://github.com/essteer/masquer/blob/main/docs/deployment.md) notes for more details.

[<h3 align="center">:arrow_up:</h3>](#title)

## Logs

TBC

[<h3 align="center">:arrow_up:</h3>](#title)

## Tests

Unit tests are contained in the `tests` directory and make use of Python's in-built `unittest` module. 

Run tests from the project root directory. To run the entire test suite use the `discover` argument:

```console
$ python3 -m unittest discover  # run all tests
......................................
----------------------------------------------------------------------
Ran 38 tests in 0.012s

OK
```

To run tests against an individual file &mdash; for example `test_assets.py` &mdash; specify the file path in the following format:

```console
$ python3 -m unittest tests.test_assets  # test a single file
...................
----------------------------------------------------------------------
Ran 19 tests in 0.002s

OK
```

### GitHub Action

A GitHub action is configured in `.github/workflows/test.yaml` to run the unit tests for any push or pull request to the `main` branch.

The tests are run on a matrix basis for Linux (Ubuntu), macOS and Windows on Python versions from `3.9` to `3.12` (inclusive).

[<h3 align="center">:arrow_up:</h3>](#title)
