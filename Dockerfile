FROM debian:buster-slim AS build
RUN apt-get update && \
  apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
  python3 -m venv /venv && \
  /venv/bin/pip install --upgrade pip

# Crea el virtualenv como un paso separado: solo vuelva a ejecutar este paso cuando los requisitos.txt cambien
FROM build AS build-venv
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

# Copiar el virtualenv en una imagen distroless
FROM gcr.io/distroless/python3-debian10

COPY --from=build-venv /venv /venv
COPY . /app
WORKDIR /app

ARG MONGO_HOST="localhost"
ARG MONGO_PORT=27017
ARG MONGO_DB="example"

ARG REDIS_HOST="localhost"
ARG REDIS_PORT=6379
ARG REDIS_DB=0

EXPOSE 9000
ENTRYPOINT ["/venv/bin/python", "index.py"]
