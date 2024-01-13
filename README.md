# Django-pagination-api

## How to setup  ###

1. copy the .env_template file and rename it to .env
2. change the path to src folder to your system absolute path
3. Run command 
```bash
docker network create djangoTest
```

## How to run  ###

```bash
docker compose up -d
```

## How to call makemigration or migrate  ###

```bash
# to call makemigrations
docker exec -it django_test /makemigration.sh

# to call migrate
docker exec -it django_test /migrate.sh
```

## How to call the unit test  ###

```bash
docker exec -it django_test /testing.sh
```

## How to fake data in the runtime database  ###

```bash
docker exec -it django_test /runcommand.sh
```