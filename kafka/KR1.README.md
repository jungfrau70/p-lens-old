cat <<EOF | tee -a ~/.bashrc
export DOCKER_HOST_IP=$(ip route get 1 | sed -n 's/^.*src \([0-9.]*\) .*$/\1/p')
EOF

for num in 1 2 3
do
    rm -rf /docker/kafka$num
    rm -rf /docker/zk$num
    mkdir -p /docker/kafka$num-data
    mkdir -p /docker/zk$num-data
    mkdir -p /docker/zk$num-txn-logs
done

source ~/.bashrc
docker-compose up -f docker-compose-kafka.yml -d

docker exec -it kafka1 kafka-topics --bootstrap-server=kafka1:9092 --create --topic telegraf-kr1-metric --partitions 2 --replication-factor 2

## (if required) Clean up
#docker-compose rm -svf