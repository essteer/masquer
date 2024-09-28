<h1 align="center" id="title">Masquer &mdash; Docker notes</h1>

<p align="center">
  Notes for use in creating, testing, and publishing the <code>masquer</code> Docker image.
</p>

## Contents

- [Overview](#overview)
- [Local development](#local-development)
  - [Test build](#test-build)
  - [Test container](#test-container)
  - [Test API on container](#test-api-on-container)
  - [Check logs on container](#check-logs-on-container)
  - [Clean up](#clean-up)
- [GitHub Action](#github-action)

See also the main [`README.md`](https://github.com/essteer/masquer/blob/main/README.md), [`development`](https://github.com/essteer/masquer/blob/main/docs/development.md) and [`deployment`](https://github.com/essteer/masquer/blob/main/docs/deployment.md) notes.

## Overview

[![Docker](https://img.shields.io/badge/Docker-masquer-2496ED.svg?flat&logo=Docker&labelColor=555&logoColor=white)](https://hub.docker.com/r/essteer/masquer)

In production `masquer` is deployed from a Docker image that is also called `masquer` and is registered here on Docker hub: [`https://hub.docker.com/r/essteer/masquer`](https://hub.docker.com/r/essteer/masquer).

The files used to configure the Docker image are both in the project root directory:

- `Dockerfile`: specifies the steps and commands to execute in the Docker image build process, as well as the top-level directory to include in the image &mdash; in this case, that is the `src` directory
- `.dockerignore`: specifies files and directories to exclude from the Docker image build


<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## Local development

During development &mdash; especially in the event of changes to the package directory structure, addition of dependencies, or changes to import statements &mdash; test builds should be created to verify that they run correctly before taking steps to integrate changes on the `main` branch or publish a new release.

In addition to testing changes to the API locally by running the FastAPI app, the API should also be thoroughly tested on a new build of the Docker image to ensure that any changes made across the package remain compatible with the container in production.

### Test build

To build a new image locally, navigate to the project root directory and change to the relevant feature branch:

```console
$ cd masquer
$ git checkout feat-example
```

Then run this command from the root level:

```console
$ docker build .  # don't miss the "."!
```

If the image fails to build, then changes are needed either to the `Dockerfile` or to the package code to make it compatible.

If the build is successful, a container can then be run using the image to test that the FastAPI app is working correctly. The last output line of a successful build will contain the `sha256` of the newly created image:

```console
=> => writing image sha256:1c3642fd9d54d5870f1ed9dfdaf75d208bee648d15ba87c6de05ja4c5c069512      0.0s
```

Note the first three characters of the image's `sha256` for subsequent use &mdash; in this case `1c3`.

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

### Test container

Use the first three characters of the image's `sha256` to launch a container, and the output will display the `sha256` of the container just created:

```console
$ docker run -d --name test-masquer -p 8000:8000 1c3
3924bff40e5aa1a567f828edd98c725a268e6843317c01185b5e454fd6b3b122
```

The `-d` argument tells Docker to run the container as a daemon (in the background).

Note the first three characters of the container's `sha256` &mdash; in this case `392`.

Run `docker ps` to confirm that the container is running:

```console
$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                    NAMES
3924bff40e5a   1c3       "fastapi run ./api/m…"   15 minutes ago   Up 15 minutes   0.0.0.0:8000->8000/tcp   test-masquer
```

The first several characters of the container's `sha256` are displayed under the `CONTAINER ID` column, as are the first three characters of the image's `sha256`.

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

### Test API on container

[![FastAPI](https://img.shields.io/badge/FastAPI-masquer-009688?style=flat&logo=FastAPI&logoColor=white)](https://masquer.fly.dev/docs)

With the container running, test a few API calls with different arguments and verify that the expected output is received, for example:

```console
$ curl -X GET 'http://127.0.0.1:8000/masq' -H 'accept: application/json'
$ curl -X GET 'http://127.0.0.1:8000/masq?ua=true&rf=true&hd=true' -H 'accept: application/json'
$ curl -X GET 'http://127.0.0.1:8000/masq?ua=true&rf=true&hd=false' -H 'accept: application/json'
```

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

### Check logs on container

If the API is working as expected, stop the container daemon and then run a shell on the container in the foreground to check that expected logs were generated.

```console
$ docker stop 392  # change '392' to match the container's ID
$ docker exec -it 392 sh  # 'sh' runs the basic shell
/usr/src/app/src $ ls
```

If successful, the terminal prompt should now display the location on the container (above, `/usr/src/app/src`).


Logs should be created on the container at `/usr/src/app/logs/app.log` &mdash; if they are not present then first make sure the path stated here is up to date with the path in the `Dockerfile`.

Change to the `logs` directory and `cat` the `app.log` contents &mdash; output similar to the lines displayed below should be visible, that relate to the previous API test calls.

```console
/usr/src/app/src $ cd ../logs
/usr/src/app/logs $ cat app.log
2024-09-22 04:34:25 - INFO - main.py:43 - FastAPI app init OK
2024-09-22 04:36:59 - INFO - routes.py:19 - Request: [ua=True rf=False hd=False]
...
```

Exit the shell to return to the main terminal.

```console
/usr/src/app/logs $ exit
$
```

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

### Clean up

If the image and container are no longer needed then clean them from the system.

Stop the container:

```console
$ docker stop 392
392  # the container ID will be repeated
```

Delete the container and the image it ran on:

```console
$ docker rm 392
392
$ docker rmi 1c3
Deleted: sha256:1c3642fd9d54d5870f1ed9dfdaf75d208bee648d15ba87c6de05ja4c5c069512
```

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>

## GitHub Action

[![GitHub](https://img.shields.io/badge/GitHub-masquer-181717.svg?flat&logo=GitHub&logoColor=white)](https://github.com/essteer/masquer)

A `docker.yaml` workflow is in place to build a new Docker image and publish it to Docker Hub whenever a new release is made on the `main` branch.

The image will be published as the latest image version listed at [`https://hub.docker.com/r/essteer/masquer`](https://hub.docker.com/r/essteer/masquer). 

For this reason, the image must be tested locally via the steps provided in this document before a new release is made to ensure that it works correctly.

<h3 align="center">
  <a href="#title"><img src="https://img.shields.io/badge/▲%20Top%20▲-0466c8.svg?style=flat"></a>
</h3>
