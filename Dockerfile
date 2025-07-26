FROM python:3.14.0rc1-alpine

LABEL maintainer="Elliott Steer <essteer@pm.me>"

WORKDIR /usr/src/app/src

RUN pip install uv

# Install FastAPI as the sole dependency
RUN uv pip install --system --no-cache fastapi==0.111.0

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
