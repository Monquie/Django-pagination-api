
#!/bin/sh

set -e
until psql -utingpay -ptingpay -htingpaydb -e 'select 1'; do
  >&2 echo "PostgresDB is unavailable - sleeping"
  sleep 1
done

  
>&2 echo "PostgresDB is up - executing command"
exec "$@"

