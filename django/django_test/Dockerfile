FROM python:3.12.0-alpine

WORKDIR /backenddjango/
COPY entrypoint.sh /entrypoint.sh
COPY makemigration.sh /makemigration.sh
COPY migrate.sh /migrate.sh
COPY runcommand.sh /runcommand.sh
COPY testing.sh /testing.sh

# COPY wait-for-db.sh /wait-for-db.sh
RUN chmod 755 /entrypoint.sh
# RUN chmod 755 /wait-for-db.sh

ENTRYPOINT ["sh", "/entrypoint.sh"]
