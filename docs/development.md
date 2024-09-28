<h1 align="center" id="title">Masquer &mdash; development</h1>

<p align="center">
  Notes for use in development, and pre-deployment testing stages.
</p>

## Contents

- [Git repository](#git-repository)
- [Asset updates](#asset-updates)
- [Docker](#docker)
- [Formatting](#formatting)
- [GitHub Actions](#github-actions)
- [Logs](#logs)
- [Tests](#tests)

See also the main [`README.md`](https://github.com/essteer/masquer/blob/main/README.md), [`deployment.md`](https://github.com/essteer/masquer/blob/main/docs/deployment.md) and [`docker.md`](https://github.com/essteer/masquer/blob/main/docs/docker.md) notes.

## Git repository

[![GitHub](https://img.shields.io/badge/GitHub-masquer-181717.svg?flat&logo=GitHub&logoColor=white)](https://github.com/essteer/masquer)

Clone the `masquer` repo for the full source code:

```console
$ git clone git@github.com:essteer/masquer
```

Create a virtual environment and install the dependencies declared in the `[project.optional-dependencies]` and `[uv.tool]` sections of `pyproject.toml` &mdash; the command below assumes a version of `uv` above `0.4.0`:

```console
$ cd masquer
$ uv sync --all-extras
```

The directory structure of the repo is as follows:

```console
.
├── .github
├── .venv
├── assets
├── dist
├── docs
├── logs
├── src
│  ├── api
│  └── masquer
│     └── utils
└── tests
```

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

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

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## Docker

[![Docker](https://img.shields.io/badge/Docker-masquer-2496ED.svg?flat&logo=Docker&labelColor=555&logoColor=white)](https://hub.docker.com/r/essteer/masquer)

In production `masquer` is deployed from a Docker image that is also called `masquer` and is registered here on Docker hub: [`https://hub.docker.com/r/essteer/masquer`](https://hub.docker.com/r/essteer/masquer).

See the separate [`docker.md`](https://github.com/essteer/masquer/blob/main/docs/docker.md) file for detailed notes on building and testing the `masquer` Docker image.

The files used to configure the Docker image are both in the project root directory:

- `Dockerfile`: specifies the steps and commands to execute in the Docker image build process, as well as the top-level directory to include in the image &mdash; in this case, that is the `src` directory
- `.dockerignore`: specifies files and directories to exclude from the Docker image build

During development &mdash; especially in the event of changes to the package directory structure, addition of dependencies, or changes to import statements &mdash; test builds should be created to verify that they run correctly before taking steps to integrate changes on the `main` branch or publish a new release.

### GitHub Action `docker.yaml`

A `docker.yaml` workflow is in place to build and publish a Docker image when a new release is made on the `main` branch &mdash; see the notes in [`deployment.md`](https://github.com/essteer/masquer/blob/main/docs/deployment.md) and [`docker.md`](https://github.com/essteer/masquer/blob/main/docs/docker.md) for more details.

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## Formatting

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Python files in `masquer` are formatted using Ruff.

### Pre-commit hook

A pre-commit hook is configured in `.pre-commit-config.yaml` to check and format files before they are committed locally. Scripts that fail the format check must be re-staged and then committed.

### GitHub Action `ruff.yaml`

A GitHub action is configured in `.github/workflows/ruff.yaml` to run Ruff checks for any push or pull request to the `main` branch.

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## GitHub Actions

[![GitHub](https://img.shields.io/badge/GitHub-masquer-181717.svg?flat&logo=GitHub&logoColor=white)](https://github.com/essteer/masquer)

GitHub actions are configured in `.github/workflows` and are in place for all pushes and pull requests for the `main` branch:

- `ruff.yaml`: checks and formats Python code (see [Formatting](#formatting))
- `test.yaml`: runs unit tests on the code in a matrix pattern (see [Tests](#tests))

A `docker.yaml` workflow is in place to build a new Docker image and publish it to Docker Hub whenever a new release is made on the `main` branch &mdash; see the [`deployment.md`](https://github.com/essteer/masquer/blob/main/docs/deployment.md) notes for more details.

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## Logs

Python's in-built `logging` module is used to log messages for `masquer`.

### Config

Log settings are configured directly within the `src` directory of the `masquer` package, and are shared by the `api` and `masquer` subdirectories that belong to the package, as well as the root-level `update.py` script that is used to fetch the latest JSON assets the package uses.

### Endpoint

A `/logs` endpoint is planned for the API so that log messages can be retrieved from the FastAPI app in production without needing to enter the Docker container.

### Format

Log messages are created with a timestamp, log level, file and line information, and then the message itself in the format:

```
YYYY-MM-DD HH:MM:SS - {log-level} - {file}:{line-number} - {message}
```

Two examples are displayed below:

```
2024-09-17 14:52:26 - INFO - routes.py:19 - Request: [ua=True rf=False hd=False count=1]
2024-09-21 13:13:34 - WARNING - app.py:29 - Invalid args: [ua='True' rf=False hd=False count=1]
```

### Output

Log messages are output to `logs/app.log`.

### Sources

The following files are set up to record log messages:

| Location | File name | Note |
| --- | --- | --- |
| `/` | `update.py` | Logs issues around updates to the JSON assets in `assets` and `src/masquer/utils/assets.py`. |
| `/` | `update.sh` | Shell script that logs output in the same format as `logging_config`. Logs issues around directory setup needed to execute the `update.py` script. |
| `src/` | `logging_config.py` | Logging setup is configured here. Logs a single message at `DEBUG` level once initialised for use in verifying log output. |
| `src/api` | `main.py` | Logs whether the initialisation of the FastAPI app was a success or failure. |
| `src/api` | `routes.py` | Logs requests and responses of the FastAPI app. |
| `src/masquer` | `app.py` | |

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

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

### GitHub Action `test.yaml`

A GitHub action is configured in `.github/workflows/test.yaml` to run the unit tests for any push or pull request to the `main` branch.

The tests are run on a matrix basis for Linux (Ubuntu), macOS and Windows on Python versions from `3.9` to `3.12` (inclusive).

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>
