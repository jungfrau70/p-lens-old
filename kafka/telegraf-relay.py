
from kafka import KafkaConsumer, KafkaProducer
import json 

KR1_TOPIC = "telegraf-kr1-metric"
KR2_TOPIC = "telegraf-kr2-metric"

kr1_brokers = ["10.11.76.177:9092", "10.11.76.177:9093", "10.11.76.177:9094"]
kr2_brokers = ["172.17.38.194:9092", "172.17.38.194:9093", "172.17.38.194:9094"]

consumer = KafkaConsumer(KR1_TOPIC, bootstrap_servers=kr1_brokers)
producer = KafkaProducer(bootstrap_servers=kr2_brokers)

for message in consumer:
  msg = json.loads(message.value.decode())
  producer.send(KR2_TOPIC, json.dumps(msg).encode("utf-8"))
