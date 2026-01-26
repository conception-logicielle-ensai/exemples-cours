FROM postgres:18

ENV POSTGRES_DB=demo_db
ENV POSTGRES_USER=demo
ENV POSTGRES_PASSWORD=demo

COPY initdb.sql /docker-entrypoint-initdb.d/init.sql