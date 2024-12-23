import json
from kafka import KafkaConsumer

# Инициализация потребителя Kafka
consumer = KafkaConsumer(
    'weather',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    group_id="weather-consumer-group",
    auto_offset_reset="earliest"
)

# Сохранение данных в файл
with open("weather_data.json", "w", encoding="utf-8") as file:
    print("Listening for messages...")
    for message in consumer:
        data = message.value
        print(f"Received: {data}")
        file.write(json.dumps(data, ensure_ascii=False) + "\n")
