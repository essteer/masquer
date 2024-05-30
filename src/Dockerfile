FROM python:3.12-alpine

LABEL maintainer="Elliott Steer <essteer@pm.me>"

WORKDIR /usr/src/app

# FastAPI is sole dependency for masquer-api
RUN pip install --no-cache-dir fastapi==0.111.0

# Copy entire src dir to WORKDIR
COPY . .

# FastAPI defaults to 8000
EXPOSE 8000

CMD [ "fastapi", "run", "./masquer_api/main.py" ]