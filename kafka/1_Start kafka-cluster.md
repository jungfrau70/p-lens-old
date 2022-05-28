# Kafka - 분산데이터스트리밍 플랫폼

References:
-. https://karthiksharma1227.medium.com/integrating-kafka-with-pyspark-845b065ab2e5

export WORKDIR='/root/PySpark/workspace/3_Kafka'
cd $WORKDIR


#########################################################################################
# 1. Configure /etc/hosts
#########################################################################################

## Add hosts
cat <<EOF | tee ./config/hosts
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

## Add hosts
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

## Ping Test
ping kafka1

#########################################################################################
# 2. Reset docker setting
#########################################################################################

## Clean Up
docker-compose rm -svf

or 
containers=`docker ps -a | grep -e 'kafka\|zoo' | awk '{print $1}'`
for container in $containers
do
    docker stop $container
    docker rm $container
done

rm -rf ./data
mkdir -p ./data/zookeeper/data
mkdir -p ./data/zookeeper/datalog
mkdir -p ./data/kafka1/data
mkdir -p ./data/kafka2/data
mkdir -p ./data/kafka3/data

## Watch services
watch docker-compose ps

## Inspect container
docker inspect kafdrop


#########################################################################################
# 3. Start kafka-cluster
#########################################################################################

docker-compose up -d

watch docker-compose ps
Every 2.0s: docker-compose ps                                                                                   Fri Apr  1 13:47:56 2022

  Name                 Command               State                                   Ports
---------------------------------------------------------------------------------------------------------------------------
kafdrop     /kafdrop.sh                      Up      0.0.0.0:9000->9000/tcp,:::9000->9000/tcp
kafka1      /etc/confluent/docker/run        Up      0.0.0.0:9091->9091/tcp,:::9091->9091/tcp, 9092/tcp
kafka2      /etc/confluent/docker/run        Up      0.0.0.0:9092->9092/tcp,:::9092->9092/tcp
kafka3      /etc/confluent/docker/run        Up      9092/tcp, 0.0.0.0:9093->9093/tcp,:::9093->9093/tcp
zookeeper   /docker-entrypoint.sh zkSe ...   Up      0.0.0.0:2181->2181/tcp,:::2181->2181/tcp, 2888/tcp, 3888/tcp, 8080/tcp


#########################################################################################
# 4. Stop kafka cluster
#########################################################################################

## Stop services
docker-compose down

## (if required) Clean up
#docker-compose rm -svf

