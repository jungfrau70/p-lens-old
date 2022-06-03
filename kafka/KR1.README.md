cat <<EOF | tee -a ~/.bashrc
export DOCKER_HOST_IP=10.11.76.177
EOF

docker-compose up -d

docker exec -it kafka1 kafka-topics --bootstrap-server=kafka1:9092 --create --topic telegraf-kr1-metric --partitions 2 --replication-factor 2
Created topic telegraf-kr1-metric.
