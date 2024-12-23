#!/bin/bash
# Запускаем Kafka
/etc/confluent/docker/run &
# Ждём, пока Kafka поднимется
sleep 10
# Создаём топик weather
kafka-topics --create --topic weather --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
# Ожидаем, чтобы контейнер оставался запущенным
tail -f /dev/null
