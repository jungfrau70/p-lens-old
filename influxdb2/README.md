rm -rf /docker/influxdb*

mkdir -p /docker/influxdb2-data
mkdir -p /docker/influxdb2-config:/etc/influxdb2

docker-compose -f docker-compose-influxdb2.yml up -d --force-recreate
