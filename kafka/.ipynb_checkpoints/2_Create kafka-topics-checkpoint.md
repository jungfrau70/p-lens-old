# Kafka - 분산데이터스트리밍 플랫폼


export WORKDIR='/root/PySpark/workspace/3_Kafka'
cd $WORKDIR

#########################################################################################
# 1. (deploy-server) Create kafka topics
#########################################################################################

## Create Topic, telegraf-kr1-metric
docker exec -it kafka1 kafka-topics --bootstrap-server=kafka1:19091 \
                                    --create \
                                    --topic telegraf-kr1-metric \
                                    --partitions 2 \
                                    --replication-factor 2

## Create Topic, telegraf-kr2-metric
docker exec -it kafka1 kafka-topics --bootstrap-server=kafka1:19091 \
                                    --create \
                                    --topic telegraf-kr2-metric \
                                    --partitions 2 \
                                    --replication-factor 2


#########################################################################################
# 2. Open kafka WebUI (=kafdrop)
#########################################################################################

## Forward a port in vscode
9000

or 
Ctrl + Shift + P, type "Forward a port"

## Open webbrowser
http://localhost:9000



## Delete topic on WebUI

## Create topic on WebUI