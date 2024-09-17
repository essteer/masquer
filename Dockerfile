FROM python:3.12-alpine

LABEL maintainer="Elliott Steer <essteer@pm.me>"

WORKDIR /usr/src/app/src

ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

# Install FastAPI as the sole dependency
RUN /root/.cargo/bin/uv pip install --system --no-cache fastapi==0.111.0

# Copy entire src directory to WORKDIR
COPY ./src .

# Create logs directory
RUN mkdir -p /usr/src/app/logs

# FastAPI defaults to port 8000
EXPOSE 8000

# Create USER
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
# Grant USER permissions to write logs
RUN chown -R appuser:appgroup /usr/src/app/logs
# Run from USER instead of ROOT
USER appuser

CMD [ "fastapi", "run", "./api/main.py" ]
