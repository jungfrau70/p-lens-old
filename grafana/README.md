rm -rf /docker/grafana-data*

mkdir -p /docker/grafana-data

or
docker volume create influxdb-volume
docker volume create grafana-volume

docker-compose -f docker-compose-grafana.yml up -d [--force-recreate]
