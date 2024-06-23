<h1 align="center">Masquer</h1>

<p align="center">
  <a href="https://github.com/essteer/masquer/actions/workflows/test.yaml"><img src="https://github.com/essteer/masquer/actions/workflows/test.yaml/badge.svg"></a>
  <a href="https://pypi.org/project/masquer/"><img src="https://img.shields.io/badge/PyPI-v1.2.0-3775A9.svg?style=flat&logo=PyPI&logoColor=white"></a>
  <a href="https://pypi.org/project/masquer/"><img src="https://img.shields.io/badge/Python-3.9_|_3.10_|_3.11_|_3.12-3776AB.svg?style=flat&logo=Python&logoColor=white"></a>
  <a href="https://snyk.io/test/github/essteer/masquer"><img src="https://snyk.io/test/github/essteer/masquer/badge.svg?name=Snyk&style=flat&logo=Snyk"></a>
</p>

<p align="center">
  <a href="https://hub.docker.com/r/essteer/masquer"><img src="https://img.shields.io/badge/Docker-2496ED.svg?flat&logo=Docker&labelColor=555&logoColor=white"></a>
  <a href="https://github.com/tiangolo/fastapi"><img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=FastAPI&labelColor=555&logoColor=white"></a>
  <a href="https://github.com/pypa/hatch"><img src="https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg"></a>
  <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"></a>
</p>

<p align="center">
A tool to generate random user-agent and referer data for GET requests.
</p>

## Overview

Use `masquer` to obtain any combination of a random user-agent, referer or header data template, then use this with a library like [`requests`](https://github.com/psf/requests) to control the session data you send to other services.

The user-agent data is drawn from [this list](https://www.useragents.me/) of the most common desktop user-agents, and referer data is taken from [this list](https://gs.statcounter.com/search-engine-market-share/desktop/worldwide) of search engines with the largest global market share.

Weighted random selections are made from those lists to approximate authentic header data patterns.

A basic header template with common attributes — like [`"Upgrade-Insecure-Requests": "1"`](https://stackoverflow.com/questions/31950470/what-is-the-upgrade-insecure-requests-http-header/32003517#32003517) — is also provided and defaults to the most common referer and user-agent data from the above lists.

### Note on privacy

Controlling header data in this way can help to preserve privacy and hinder third-party tracking behaviour, by blending part of your web profile with the most common configurations. 

It does not provide anonymity — that is a much more complex topic, and the open-source [Privacy Guides](https://www.privacyguides.org/en/) are a good place to start.

## Installation

To get hold of `masquer` either install the PyPI package into your project's virtual environment, clone the GitHub repo or pull the Docker image.

### PyPI package

[![](https://img.shields.io/badge/PyPI-masquer-3775A9.svg?style=flat&logo=PyPI&logoColor=white)](https://pypi.org/project/masquer/)

Install the `masquer` package from PyPI to retrieve just the tool with no extras.

Activate your existing project's virtual environment, then download `masquer` using a package manager. The below example uses [Astral's](https://astral.sh/blog/uv) `uv`; substitute `pip` by dropping "`uv`" or use another package manager as needed: 

```console
$ uv pip install masquer
```

### GitHub repo

[![](https://img.shields.io/badge/GitHub-masquer-181717.svg?flat&logo=GitHub&logoColor=white)](https://github.com/essteer/masquer)

Clone the `masquer` repo from GitHub for the full source code. The repo includes the JSON source files used to generate the header data, a script to sync the programme if updates are made to the JSON files, and a test suite.

```console
$ git clone git@github.com:essteer/masquer
```

The functional code within the package `src` directory has no dependencies beyond Python built-in modules. If you intend to make changes to your cloned version of the repo, you may optionally install the `project.optional-dependencies` declared in the `pyproject.toml` file.

First create and activate a virtual environment — the below example uses [Astral's](https://astral.sh/blog/uv) `uv`; substitute `pip` or use another package manager as needed — then install the `dev` dependencies:

![](https://img.shields.io/badge/Linux-FCC624.svg?style=flat&logo=Linux&logoColor=black)
![](https://img.shields.io/badge/macOS-000000.svg?style=flat&logo=Apple&logoColor=white)

```console
$ uv venv
$ source .venv/bin/activate
$ uv pip install fastapi==0.111.0 hatchling==1.24.2 pre-commit==3.7.1 ruff==0.4.4
```

![](https://img.shields.io/badge/Windows-0078D4.svg?style=flat&logo=Windows&logoColor=white)

```console
$ uv venv
$ .venv\Scripts\activate
$ uv pip install fastapi==0.111.0 hatchling==1.24.2 pre-commit==3.7.1 ruff==0.4.4
```

### FastAPI

[![FastAPI](https://img.shields.io/badge/FastAPI-masquer_API-009688?style=flat&logo=FastAPI&logoColor=white)](https://masquer.fly.dev/docs)

The GitHub repo includes `masquer API`, a FastAPI version of `masquer`.

To self-host the API, install the `FastAPI` optional dependency as declared in the `pyproject.toml` file. 

Activate the API from the root directory via:

```console
$ fastapi run src/masquer_api/main.py
```

Then follow the instructions provided by FastAPI in the terminal.

By default, the FastAPI app will run on localhost. To view the API documentation, run the API and navigate to `http://127.0.0.1:8000/docs`.

### Docker image

[![Docker](https://img.shields.io/badge/Docker-masquer-2496ED.svg?flat&logo=Docker&labelColor=555&logoColor=white)](https://hub.docker.com/r/essteer/masquer)

For no good reason, the `masquer API` is also available as a `Docker` image:

```console
$ docker pull essteer/masquer
```

## Operation

[![](https://img.shields.io/badge/PyPI-masquer-3775A9.svg?style=flat&logo=PyPI&logoColor=white)](https://pypi.org/project/masquer/)
[![](https://img.shields.io/badge/GitHub-masquer-181717.svg?flat&logo=GitHub&logoColor=white)](https://github.com/essteer/masquer)

Interact with `masquer` via the `masq` method:

```python
from masquer import masq
```

The `masq` function accepts up to three boolean parameters:

```python
useragent = masq(
  ua = True,  # user-agent, defaults to True
  rf = False,  # referer, defaults to False
  hd = False,  # header-data, defaults to False
)
```

And returns the response in dictionary form:

```python
{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3'}
```

### FastAPI

[![FastAPI](https://img.shields.io/badge/FastAPI-masquer_API-009688?style=flat&logo=FastAPI&logoColor=white)](https://masquer.fly.dev/docs)

`masquer API` is deployed on Fly.io - view the docs at [`https://masquer.fly.dev/docs`](https://masquer.fly.dev).

An example of how to use `masquer API`:

```bash
$ curl -X GET \
  'https://masquer.fly.dev/masq?ua=true&rf=false&hd=false' \
  -H 'accept: application/json'
```

### Docker

[![Docker](https://img.shields.io/badge/Docker-masquer-2496ED.svg?flat&logo=Docker&labelColor=555&logoColor=white)](https://hub.docker.com/r/essteer/masquer)

Run the `masquer API` from a container on the `masquer` Docker image as follows:

```console
$ docker run -d --name masquer -p 8000:8000 esteer/masquer
```

Then interact as per the FastAPI instructions above.

### Examples

#### User-agent only

By default only `ua` is set to `True`, so each of the following methods may be used to return just one randomly generated user-agent:

```python
>>> useragent_1 = masq()
>>> useragent_2 = masq(True)
>>> useragent_3 = masq(ua=True)
>>>
>>> useragent_1
{"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.3"}
>>> useragent_2
{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0."}
>>> useragent_3
{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.3"}
```

#### Referer only

By the same logic, these methods will each return just one randomly generated referer:

```python
>>> referer_1 = masq(False, True)
>>> referer_2 = masq(ua=False, rf=True)
>>> referer_3 = masq(ua=False, rf=True, hd=False)
>>>
>>> referer_1
{"Referer": "https://www.google.com/"}
>>> referer_2
{"Referer": "https://www.google.com/"}
>>> referer_3
{"Referer": "https://bing.com/"}
```

#### Header-data

By default, the header data template supplies the most common user-agent and referer values as fixed, and can be accessed via the following methods:

```python
>>> default_header_1 = masq(False, False, True)
>>> default_header_2 = masq(ua=False, hd=True)
>>> default_header_3 = masq(ua=False, rf=False, hd=True)
>>>
>>> default_header_1 == default_header_2 == default_header_3
True
>>> default_header_1
{"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.5;", "Referer": "https://www.google.com/", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.3"}
```

As per the individual use-cases, get weighted random user-agent and referer values in the header by omitting the `ua` value (which defaults to `True`) and setting `rf` to `True`. A non-exhaustive selection of examples is provided below:

```python
>>> # header with random user-agent and fixed referer
>>> random_header_1 = masq(hd=True)  
>>> random_header_2 = masq(True, False, True)
>>>
>>> # header with fixed user-agent and random referer
>>> random_header_3 = masq(False, True, True)
>>> random_header_4 = masq(ua=False, rf=True, hd=True)
>>>
>>> # header with random user-agent and random referer
>>> random_header_5 = masq(rf=True, hd=True)
>>> random_header_6 = masq(True, True, True)
```

## Local development

The following details will assist with making and testing changes to a cloned version of the repository.

### Updates

The root directory includes a shell script `update.sh` for convenience to update JSON assets for the `masquer` package.

If using your own JSON data you can still make use of the `update_assets()` function inside `update.py` to sync changes with the `assets.py` file inside the `masquer` package by running `update.py` from the terminal:

![](https://img.shields.io/badge/Linux-FCC624.svg?style=flat&logo=Linux&logoColor=black)

```console
$ chmod +x update.sh
$ ./update.sh
Update successful
```

### Tests

`masquer` uses Python's in-built `unittest` module. 

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
