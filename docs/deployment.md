<h1 align="center" id="title">Masquer &mdash; deployment</h1>

<p align="center">
  Notes for use in deployment.
</p>

The most frequent releases for `masquer` consist only of updates to the JSON assets and `assets.py` contents. Since these updates do not introduce functional changes, they are treated as micro releases. 

The process for more significant releases may be more involved in the development stages, but the subsequent stages from testing onwards should remain the same.

## Contents

- [Micro releases](#micro-releases)
  - [Create feature branch](#create-feature-branch)
  - [Update assets](#update-assets)
- [Test](#test)
  - [Unit tests](#unit-tests)
  - [API tests](#api-tests)
  - [Docker image tests](#docker-image-tests)
- [Version](#version)
- [Format](#format)
- [Build distribution](#build-distribution)
- [Merge to main](#merge-to-main)
- [Release-and-build Docker image](#release-and-build-docker-image)
  - [Pull image and run container](#pull-image-and-run-container)
- [Publish to PyPI](#publish-to-pypi)
- [Deploy to production](#deploy-to-production)

See also the main [`README.md`](https://github.com/essteer/masquer/blob/main/README.md), [`development.md`](https://github.com/essteer/masquer/blob/main/docs/development.md) and [`docker.md`](https://github.com/essteer/masquer/blob/main/docs/docker.md) notes.

## Micro releases

Asset updates are performed on a regular basis to keep the user-agent and referer data current. These are treated as micro releases.

A typical workflow up to the testing stage is outlined in this section.

Activate the virtual environment then create and checkout a new branch such as `asset-update`.

```console
$ source .venv/bin/activate
$ git branch asset-update
$ git checkout asset-update
Switched to branch 'asset-update'
```

### Update assets

For an asset update, follow the instructions detailed under the [`Asset updates`](https://github.com/essteer/masquer/blob/main/docs/development.md#asset-updates) section of `development.md`.

If the process is successful and no issues arose, continue to the testing stage.

<h3 align="center">
  <a href="#"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## Test

Follow these sections in sequence and ensure that the tests for each stage are passing before proceeding to the next stage.

For new features, new unit tests will have been introduced that must pass in addition to all existing tests.

### Unit tests

First run all unit tests as detailed under the [`Tests`](https://github.com/essteer/masquer/blob/main/docs/development.md#tests) section of `development.md`.

Ensure all tests are passing before proceeding further.

### API tests

<a href="https://github.com/tiangolo/fastapi"><img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=FastAPI&labelColor=555&logoColor=white"></a>

Once the unit tests have passed, run the FastAPI app from the project root directory in development mode:

```console
$ fastapi dev src/api/main.py
```

If the app launches successfully, visit the documentation link provided and test the API is functioning as expected &mdash; this will be [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) unless a different port number was specified.

If the tests work from the documentation, make a `curl` request from a separate terminal window:

```console
$ curl -X GET 'http://127.0.0.1:8000/api/v1/masq?ua=true&rf=true' -H 'accept: application/json'
```

If the expected response is received, proceed to the Docker image tests.

### Docker image tests

<a href="https://hub.docker.com/r/essteer/masquer"><img src="https://img.shields.io/badge/masquer-2496ED.svg?flat&logo=Docker&labelColor=555&logoColor=white"></a>

Follow the steps detailed in [`docker.md`](https://github.com/essteer/masquer/blob/main/docs/docker.md) to build and test a Docker image locally.

Once the image and container are confirmed as running successfully, repeat the API tests to ensure those behave as expected as well.

If each of the steps indicated above is successful, deployment can proceed to the next stage.

<h3 align="center">
  <a href="#"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## Version

[![Hatch](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

Increment the version for a micro, minor or major release:

```console
$ hatch version micro
Old: 1.2.1
New: 1.2.2
```

This will automatically update the version number in `src/masquer/__about__.py`, which is where the version information in `pyproject.toml` is read from for the main `masquer` program, and in `src/api/main.py` for the API.

Manually update the version number in the PyPI icon at the top of [`README.md`](https://github.com/essteer/masquer/blob/main/README.md) to match the new version number.

<h3 align="center">
  <a href="#"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## Format

 <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"></a>

Add and commit the version changes to git. 

Ruff is configured as a pre-commit hook to lint and format the package. Ruff will format files that aren't already in the correct format &mdash; those files will fail the check, so run all unit tests once again to be sure nothing was broken then add and commit the reformatted files.

See the [`Formatting`](https://github.com/essteer/masquer/blob/main/docs/development.md#formatting) section of [`development.md`](https://github.com/essteer/masquer/blob/main/docs/development.md) for more details.

(Note that if a more significant feature is in development, it will involve multiple commits to the feature branch over time. Format checks will therefore take place with each commit.)

Push to GitHub.

<h3 align="center">
  <a href="#"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## Merge to `main`

[![](https://img.shields.io/badge/GitHub-masquer-181717.svg?flat&logo=GitHub&logoColor=white)](https://github.com/essteer/masquer)

If the package build was successful, open a PR on GitHub to merge the updated package into `main` branch. 

GitHub workflows are in place to do a final format and test whenever a commit or PR is made into `main`. 

See the [`GitHub Actions`](https://github.com/essteer/masquer/blob/main/docs/development.md#github-actions) section of [`development.md`](https://github.com/essteer/masquer/blob/main/docs/development.md) for more details. 

<h3 align="center">
  <a href="#"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## Release and build Docker image

[![](https://img.shields.io/badge/GitHub-masquer-181717.svg?flat&logo=GitHub&logoColor=white)](https://github.com/essteer/masquer)
<a href="https://hub.docker.com/r/essteer/masquer"><img src="https://img.shields.io/badge/masquer-2496ED.svg?flat&logo=Docker&labelColor=555&logoColor=white"></a>

Assuming that the PR passed the GitHub Actions and the merge completed successfully, from the [main repo page](https://github.com/essteer/masquer) on GitHub click on the `Releases` heading then `Draft a new release`.

From the `Choose a tag` dropdown enter the new version number in the format `v0.1.0`, then click `Generate release notes` to automatically include information on changes made since the previous release.

Add any other necessary comments then click `Publish release`.

The `docker.yaml` GitHub workflow will then build a Docker image of the new version and push the build to [Docker Hub](https://hub.docker.com/r/essteer/masquer).

### Pull image and run container

Follow the instructions in [`docker.md`](https://github.com/essteer/masquer/blob/main/docs/docker.md) to pull and test that the image is working as expected.

<h3 align="center">
  <a href="#"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## Build distribution

[![Hatch](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

Navigate to the project root directory and run `$ hatch build` from the terminal to build the `sdist` and `wheel` targets inside the `dist/` directory.

```console
$ hatch build
────────────── sdist ──────────────
dist/masquer-1.2.2.tar.gz
────────────── wheel ──────────────
dist/masquer-1.2.2-py3-none-any.whl
```

<h3 align="center">
  <a href="#"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## Publish to PyPI

<a href="https://pypi.org/project/masquer/"><img src="https://img.shields.io/badge/PyPI-3775A9.svg?style=flat&labelColor=555&logo=PyPI&logoColor=white"></a>

After a successful build the package is ready to publish on PyPI:

```console
$ python3 -m twine upload dist/*
Uploading distributions to https://upload.pypi.org/legacy/
Uploading masquer-1.2.2-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 32.1/32.1 kB • 00:00 • 7.3 MB/s
Uploading masquer-1.2.2.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 31.0/31.0 kB • 00:00 • 15.5 MB/s

View at:
https://pypi.org/project/masquer/1.2.2/
```

<h3 align="center">
  <a href="#"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## Deploy to production

<a href="https://masquer.fly.dev/docs"><img src="https://img.shields.io/badge/Fly.io-24175B.svg?style=flat&labelColor=555&logo=flydotio&logoColor=white"></a>


From the project root directory, run the following command to deploy to production:

```console
$ fly deploy
```

Visit the deployment at the link as prompted and test it via the API docs.

<h3 align="center">
  <a href="#"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>
