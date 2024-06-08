FROM python:3.12-alpine

LABEL maintainer="Elliott Steer <essteer@pm.me>"

WORKDIR /usr/src/app

ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh
# FastAPI is sole dependency for masquer-api
RUN /root/.cargo/bin/uv pip install --system --no-cache fastapi==0.111.0

# Copy entire src dir to WORKDIR
COPY ./src .

# FastAPI defaults to 8000
EXPOSE 8000

# Don't use ROOT
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

CMD [ "fastapi", "run", "./masquer_api/main.py" ]