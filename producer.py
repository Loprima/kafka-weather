import json
import random
import time
from kafka import KafkaProducer

# Список городов и погодных условий
cities = ["Moscow", "Saint Petersburg", "Krasnoyarsk", "Sochi", "Vladivostok"]
conditions = ["sunny", "rainy", "cloudy", "snowy", "windy"]

# Инициализация продюсера Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Отправка сообщений
try:
    while True:
        city = random.choice(cities)
        weather_data = {
            "city": city,
            "temperature": random.randint(-30, 35),
            "condition": random.choice(conditions)
        }
        producer.send("weather", value=weather_data)
        print(f"Sent: {weather_data}")
        time.sleep(1)  # Задержка для имитации реального времени
except KeyboardInterrupt:
    print("Producer stopped.")
finally:
    producer.close()
