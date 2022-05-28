# Kafka - 분산데이터스트리밍 플랫폼

References:
-. https://enowy.tistory.com/m/12

export WORKDIR='/root/lens/influx'
cd $WORKDIR


#########################################################################################
# 1. Configure /etc/hosts
#########################################################################################

## Add hosts
cat <<EOF | tee -a /etc/hosts

172.18.0.19     influx
EOF

## Ping Test
ping influx

#########################################################################################
# 2. Reset docker setting
#########################################################################################

## Clean Up
docker-compose rm -svf

or 
containers=`docker ps -a | grep -e 'influx' | awk '{print $1}'`
for container in $containers
do
    docker stop $container
    docker rm $container
done

rm -rf ./data

mkdir -p ./data/influxdb2-data
mkdir -p ./data/influxdb2-config
mkdir -p ./data/grafana-data
mkdir -p ./data/telegraf/
chown -R 472:472 ./data/grafana-data

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
docker-compose down --remove-orphans

## (if required) Clean up
#docker-compose rm -svf

