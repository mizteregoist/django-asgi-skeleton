First init
```
cd project
cd app
PIPENV_VENV_IN_PROJECT=1 pipenv install --python 3.9 -r requirements.txt
rm -rf .venv
```

При разворачивании в докере local version:

```
cd project

docker-compose -f docker-compose.local.yml up -d --build
set ENV variables like in localserver configuration
NGINX_PORT_HTTP_DEV=
PGSQL_USER=
PGSQL_PASS=
PGSQL_NAME=
```

При разворачивании в докере dev version:

```
cd project

docker-compose -f docker-compose.dev.yml up -d --build
set ENV variables
NGINX_PORT_HTTP_DEV=
PGSQL_USER=
PGSQL_PASS=
PGSQL_NAME=
```

При разворачивании в докере prod version:

```
cd project

docker-compose -f docker-compose.prod.yml up -d --build
set ENV variables
NGINX_PORT_HTTP=
PGSQL_USER=
PGSQL_PASS=
PGSQL_NAME=
```

Необходимые переменные в .env файле:

```
NGINX_PORT_HTTP=
NGINX_PORT_HTTP_DEV=

PGSQL_NAME=
PGSQL_PASS=
PGSQL_USER=
```

DIRECTORY STRUCTURE
-------------------

```
app
    app/
    error/
    frontend/
docker
    config/              contains shared configurations
    logs/                contains container logs
```
