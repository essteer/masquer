# Deployment

[![Hatch](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

Asset updates are performed on a regular basis to keep the user-agent and referer data current. The instructions that follow are written with these micro releases in mind, but the process will be similar for feature releases.

Activate the virtual environment then create and checkout a new branch such as `asset-update`.

![](https://img.shields.io/badge/Linux-FCC624.svg?style=flat&logo=Linux&logoColor=black)

```console
$ source .venv/bin/activate
$ git branch asset-update
$ git checkout asset-update
Switched to branch 'asset-update'
```

### Update

For an asset update, follow the [update instructions](#updates).

### Test

Ensure all tests are passing before proceeding further. See the [Tests section](#tests) above.

### Version

Increment the version for a micro, minor or major release:

```console
$ hatch version micro
Old: 1.2.1
New: 1.2.2
```

This will automatically update the version number in `src/masquer/__about__.py`, which is where the version information in `pyproject.toml` is read from for the main `masquer` program, and in `src/api/main.py` for the API.

Manually update the version number in the PyPI icon at the top of this README to match the new version number.

### Format

Add and commit the version changes to git. Ruff is configured as a pre-commit hook to lint and format the package. Ruff will format files that aren't already in the correct format &mdash; those files will fail the check, so run all unit tests once again to be sure nothing was broken then add and commit the reformatted files.

Push the branch to GitHub.

### Build

Run `$ hatch build` from the terminal to build the `sdist` and `wheel` targets inside the `dist/` directory.

```console
$ hatch build
────────────── sdist ──────────────
dist/masquer-1.2.2.tar.gz
────────────── wheel ──────────────
dist/masquer-1.2.2-py3-none-any.whl
```

### Publish

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

### Merge to `main`

Open a PR on GitHub to merge the updated package into `main` branch. GitHub workflows are in place to do a final format and test whenever a commit or PR is made into `main`.

### Release and build Docker image

From the [main repo page](https://github.com/essteer/masquer) on GitHub click on the `Releases` heading then `Draft a new release`.

From the `Choose a tag` dropdown enter the new version number in the format `v0.1.0`, then click `Generate release notes` to automatically include information on changes made since the previous release.

Add any other necessary comments then click `Publish release`.

The `docker.yaml` GitHub workflow will then build a Docker image of the new version and push the build to [Docker Hub](https://hub.docker.com/r/essteer/masquer).