rm -rf /docker/grafana-data*

mkdir -p /docker/grafana-data

docker-compose -f docker-compose-grafana.yml up -d [--force-recreate]
