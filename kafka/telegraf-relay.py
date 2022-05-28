
from kafka import KafkaConsumer, KafkaProducer
import json 

KR1_TOPIC = "telegraf-kr1-metric"
KR2_TOPIC = "telegraf-kr2-metric"

brokers = ["kafka1:19091", "kafka2:19092", "kafka3:19093"]

consumer = KafkaConsumer(KR1_TOPIC, bootstrap_servers=brokers)
producer = KafkaProducer(bootstrap_servers=brokers)

for message in consumer:
  msg = json.loads(message.value.decode())
  producer.send(KR2_TOPIC, json.dumps(msg).encode("utf-8"))
