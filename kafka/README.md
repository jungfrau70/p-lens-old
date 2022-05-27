

cat <<EOF | tee /etc/hosts
127.0.0.1       localhost
127.0.1.1       ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

172.18.0.80     zookeeper
172.18.0.81     kafka1
172.18.0.82     kafka2
172.18.0.83     kafka3
172.18.0.84     kafdrop
EOF

rm -rf ./data
mkdir -p ./data/zookeeper/data
mkdir -p ./data/zookeeper/datalog
mkdir -p ./data/kafka1/data
mkdir -p ./data/kafka2/data
mkdir -p ./data/kafka3/data

docker-compose up -d



#########################################################################################
# 3. (deploy-server) Hands on in kafka custer
#########################################################################################

## Create New Topic
docker exec -it kafka1 kafka-topics --bootstrap-server=kafka1:19091 \
                                    --create \
                                    --topic telegraf-kr1-metric \
                                    --partitions 2 \
                                    --replication-factor 2

