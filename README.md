<h1 align="center" id="title">Masquer</h1>

<p align="center">
  <a href="https://github.com/essteer/masquer/actions/workflows/test.yaml"><img src="https://github.com/essteer/masquer/actions/workflows/test.yaml/badge.svg"></a>
  <a href="https://pypi.org/project/masquer/"><img src="https://img.shields.io/pypi/v/masquer?style=flat&logo=PyPI&logoColor=white&label=PyPI&labelColor=555&color=3776AB"></a>
  <a href="https://pypi.org/project/masquer/"><img src="https://img.shields.io/badge/Python-3.9_~_3.13-3776AB.svg?style=flat&logo=Python&logoColor=white"></a>
  <a href="https://snyk.io/test/github/essteer/masquer"><img src="https://snyk.io/test/github/essteer/masquer/badge.svg?name=Snyk&style=flat&logo=Snyk"></a>
</p>

<p align="center">
  <a href="https://astral.sh"><img src="https://img.shields.io/badge/Astral-261230.svg?style=flat&logo=Astral&labelColor=555&logoColor=white"></a>
  <a href="https://hub.docker.com/r/essteer/masquer"><img src="https://img.shields.io/badge/Docker-2496ED.svg?flat&logo=Docker&labelColor=555&logoColor=white"></a>
  <a href="https://github.com/tiangolo/fastapi"><img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=FastAPI&labelColor=555&logoColor=white"></a>
  <a href="https://masquer.fly.dev/docs"><img src="https://img.shields.io/badge/Fly.io-24175B.svg?style=flat&labelColor=555&logo=flydotio&logoColor=white"></a>
  <a href="https://github.com/pypa/hatch"><img src="https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg"></a>
</p>

<p align="center">
A tool to generate random user-agent and referer data for HTTP requests.
</p>

## Overview

Use `masquer` to obtain any combination of a random user-agent, referer or header data template, then use this with a library like [`requests`](https://github.com/psf/requests) to control the session data you send to other services.

The user-agent data is drawn from [this list](https://www.useragents.me/) of the most common desktop user-agents, and referer data is taken from [this list](https://gs.statcounter.com/search-engine-market-share/desktop/worldwide) of search engines with the largest global market share.

Weighted random selections are made from those lists to approximate authentic header data patterns.

A basic header template with common attributes — like [`"Upgrade-Insecure-Requests": "1"`](https://stackoverflow.com/questions/31950470/what-is-the-upgrade-insecure-requests-http-header/32003517#32003517) — is also provided and defaults to the most common referer and user-agent data from the above lists.

### Note on privacy

Controlling header data in this way can help to preserve privacy and hinder third-party tracking behaviour by blending part of your web profile with the most common configurations. 

It does not provide anonymity — that is a much more complex topic, and the open-source [Privacy Guides](https://www.privacyguides.org/en/) are a good place to start.

## Documentation

The sections that follow describe different ways to use `masquer`.

For development purposes see the `docs` directory for notes on development, deployment and Docker.

- [API](#api)
- [Python package](#python-package)
  - [Installation](#installation)
  - [Operation](#operation)
  - [Examples](#examples)
- [Git repository](#git-repository)
- [Docker image](#docker-image)

## API

[![FastAPI](https://img.shields.io/badge/FastAPI-masquer-009688?style=flat&logo=FastAPI&logoColor=white)](https://masquer.fly.dev/docs)

An API for `masquer` is in deployment at `https://masquer.fly.dev/masq` &mdash; try it out with the interactive [Swagger UI](https://masquer.fly.dev/docs) or [ReDoc](https://masquer.fly.dev/redoc) documentation.

The API returns a JSON array, making it compatible with any language that can make HTTP requests and parse JSON.

Here is an example using `curl` from the command line to get a random user-agent and referer:

```console
$ curl -X GET 'https://masquer.fly.dev/api/v1/masq?ua=true&rf=true' -H 'accept: application/json'
[
  {
    "Referer":"https://www.google.com",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.3"
  }
]
```

The optional `count` parameter specifies the number of objects to return in the response. The default value is `1`.

Refer to the [API docs](`https://masquer.fly.dev/docs`) for other examples, or see [more details below](#examples) in the package documentation.

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## Python package

[![PyPI](https://img.shields.io/badge/PyPI-masquer-3775A9.svg?style=flat&logo=PyPI&logoColor=white)](https://pypi.org/project/masquer/)

### Installation

To use the `masquer` Python package, create and activate a virtual environment then install `masquer` using a package manager.

The below example uses [Astral's](https://docs.astral.sh/uv) `uv` &mdash; substitute `pip` by dropping "`uv`" or use another package manager as preferred:

```console
$ uv venv
$ source .venv/bin/activate
$ uv pip install masquer
```

The core tool obtained this way has no dependencies.

### Operation

Interact with `masquer` via the `masq` method:

```python
>>> from masquer import masq
```

The `masq` function accepts up to three boolean parameters...

```python
>>> useragent = masq(
  ua = True,  # user-agent, defaults to True
  rf = False,  # referer, defaults to False
  hd = False  # header-data, defaults to False
)
```

...and returns the response as a dict object:

```python
{
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.'
}
```

### Examples

#### User-agent

By default only the `ua` parameter is set to `True`, so each of the following methods may be used to obtain just one randomly selected user-agent:

```python
>>> masq()
{"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.3"}
>>> masq(True)
{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0."}
>>> masq(ua=True)
{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.3"}
```

#### Referer

By the same logic, the following methods will each return one randomly selected referer:

```python
>>> masq(False, True)
{"Referer": "https://www.google.com/"}
>>> masq(ua=False, rf=True)
{"Referer": "https://www.google.com/"}
>>> masq(ua=False, rf=True, hd=False)
{"Referer": "https://bing.com/"}
```

#### Header-data with default user-agent and referer

The default header-data template supplies the most common user-agent and refer values as fixed values, and can be accessed via the following methods:

```python
>>> masq(False, False, True)
>>> masq(ua=False, hd=True)
>>> masq(ua=False, rf=False, hd=True)
```

Each of the above function calls would return the following:

```python
>>> default_header = masq(ua=False, rf=False, hd=True)
>>> default_header
{
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
  "Accept-Encoding": "gzip, deflate, br", 
  "Accept-Language": "en-US,en;q=0.5;", 
  "Referer": "https://www.google.com/", 
  "Sec-Fetch-Dest": "document", 
  "Sec-Fetch-Mode": "navigate", 
  "Sec-Fetch-Site": "none", 
  "Sec-Fetch-User": "?1", 
  "Upgrade-Insecure-Requests": "1", 
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.3"
}
```

#### Header-data with random user-agent and referer

To get the header-data with randomly selected user-agent and/or referer data, pass those arguments as `True` in addition to the `hd` parameter as per the below examples:

```python
>>> random_header = masq(rf=True, hd=True)  # ua=True by default
>>> random_header
{
  # ...
  "Referer": "https://duckduckgo.com",
  # ...
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113."
}
```

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## Git repository

[![GitHub](https://img.shields.io/badge/GitHub-masquer-181717.svg?flat&logo=GitHub&logoColor=white)](https://github.com/essteer/masquer)

Clone the `masquer` repo for the full source code, including the FastAPI app used to host the [API](#api) introduced above. 

The repo includes the JSON source files used to generate the header data, a script to update the JSON content to the latest data, and a test suite.

```console
$ git clone git@github.com:essteer/masquer
```

The package code within the `src/masquer` directory has no dependencies beyond built-in Python modules, so can be run right away in a virtual environment.

The `update.sh` shell script in the root directory updates the `header.json` and `referer.json` files in the `assets` directory to the latest versions, then uses this data to update the `assets.py` file used by the `masquer` package.

To use the `update.sh` script first install Beautiful Soup into the virtual environment:

```console
$ source .venv/bin/activate
$ uv pip install beautifulsoup4==4.12.3
```

Then grant execution permissions to `update.sh` and run it &mdash; the output should appear similar to that displayed below:

```console
$ chmod +x update.sh
$ ./update.sh
2024-09-17 14:34:03 - INFO - update.py:29 - Fetched user-agent data
2024-09-17 14:34:04 - INFO - update.py:74 - Fetched referer data
2024-09-17 14:34:04 - INFO - update.py:133 - Saved user-agent and referer JSON data to assets.py
2024-09-17 14:34:04 - INFO - update.sh - Asset update OK
```

If interested in making changes to the repo, see the `development notes` for additional details.

### FastAPI

[![FastAPI](https://img.shields.io/badge/FastAPI-masquer-009688?style=flat&logo=FastAPI&logoColor=white)](https://masquer.fly.dev/docs)

The Git repo includes the [FastAPI version](#api) of `masquer` that is introduced above and hosted at [`https://masquer.fly.dev`](https://masquer.fly.dev/docs) &mdash; the relevant code is located at `src/api`.

To self-host the API, install the `FastAPI` optional dependency as declared in the `pyproject.toml` file. 

```console
$ source .venv/bin/activate
$ uv pip install fastapi==0.111.0
```

FastAPI runs on localhost port `8000` by default &mdash; to amend this change the relevant uvicorn argument in `src/api/main.py`:

```python
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
```

Run the app from the root directory via:

```console
$ fastapi run src/api/main.py
```

Then follow the instructions FastAPI provides in the terminal.

To view the API's interactive documentation, run the app and navigate to `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc`.

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## Docker image

[![Docker](https://img.shields.io/badge/Docker-masquer-2496ED.svg?flat&logo=Docker&labelColor=555&logoColor=white)](https://hub.docker.com/r/essteer/masquer)

A Docker image for `masquer` has been developed for production use, and is publicly available.

To run `masquer` from a container, first pull the image from [DockerHub](https://hub.docker.com/r/essteer/masquer):

```console
$ docker pull essteer/masquer
```

Launch a container using the `masquer` image as follows:

```console
$ docker run -d --name masquer -p 8000:8000 essteer/masquer
```

Then interact as per the [API instructions](#api) above.

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>
