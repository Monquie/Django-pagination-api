
#!/bin/sh

set -e
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "django_postgres" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  >&2 echo "PostgresDB is unavailable - sleeping"
  sleep 1
done

  
>&2 echo "PostgresDB is up - executing command"
exec "$@"

