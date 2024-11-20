#!/bin/bash

# Comando para publicar el mensaje del sensor usando mosquitto_pub

mosquitto_pub -h 127.0.0.1 -p 1883 -t "iot/sensor/luz" -m '{
    "device_id": "5ee9df89-a719-4e9a-ac54-84b9c3096f40", 
    "event_time": "2024-11-19T15:00:00Z", 
    "value": 45, 
    "accuracy": 0.95
}'

# Puedes agregar más comandos de publicación con diferentes valores
# si deseas simular varios valores de sensor, por ejemplo:
# 
# mosquitto_pub -h 127.0.0.1 -p 1883 -t "iot/sensor/luz" -m '{
#     "device_id": "5ee9df89-a719-4e9a-ac54-84b9c3096f40", 
#     "event_time": "2024-11-19T15:05:00Z", 
#     "value": 60, 
#     "accuracy": 0.98
# }'

echo "Mensaje enviado al broker MQTT"
