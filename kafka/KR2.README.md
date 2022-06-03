cat <<EOF | tee -a ~/.bashrc
export DOCKER_HOST_IP=172.17.37.239
EOF

docker-compose up -d

docker exec -it kafka1 kafka-topics --bootstrap-server=kafka1:9092 --create --topic telegraf-kr2-metric --partitions 2 --replication-factor 2
