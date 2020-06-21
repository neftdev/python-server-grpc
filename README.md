# Servidor GRPC con Python

python-server-grpc es una aplicación realizado para el proyecto 2 del curso de Sistemas Operativos.
Este servidor se conecta con el cliente [go-client-grpc](https://github.com/NeftXx/go-client-grpc).

## Construir imagen

Primero es loguearse con docker login, ingresando su usuario y contraseña de DockerHub:

```bash
docker login
```

Luego debemos construir la imagen, con el siguiente comando:

```bash
docker build -t python-server-grpc .
```

Luego tagueamos la imagen local con nuestro usuario y el repositorio de docker hub.

> Nota: \$1 es el tu nombre de usuario de docker hub

```bash
docker tag python-server-grpc $1/python-server-grpc
```

Por ultimo, subimos la imagen al repositorio

```bash
docker push $1/python-server-grpc
```

Si deseas puedes usar el script [build-docker.sh](build-docker.sh) dandole permisos de ejecución, ejecutandoló y mandando de parámetro el nombre del usuario del DockerHub (Debes estar en la carpeta del Dockerfile).

```bash
chmod 777 build-docker.sh
build-docker.sh usuarioDockerHub
```

## Como usar la imagen

El siguiente ejemplo, crea un servidor en el puerto 9000.

```bash
docker run -d --name python-server -p 9000:9000 neftxx/python-server-grpc
```

### Configuración

Las variables de entorno se pasan al comando de ejecución para configurar un contenedor.

| Nombre     | Valor por defecto | Descripción                                                 |
| ---------- | ----------------- | ----------------------------------------------------------- |
| MONGO_HOST | "localhost"       | HOST donde se encuentra alojado la base de datos de MongoDB |
| MONGO_PORT | 27017             | Puerto de MongoDB                                           |
| MONGO_DB   | "example"         | Nombre de la base de datos                                  |

#### Ejemplo

```bash
docker run -d \
  --name python-server \
  -p 9000:9000 \
  -e MONGO_HOST="localhost" \
  -e MONGO_PORT=27017 \
  -e MONGO_DB="example" \
  neftxx/python-server-grpc
```
