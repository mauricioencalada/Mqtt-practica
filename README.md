# IoT MQTT Sensor Simulation
Este proyecto simula un sistema IoT usando MQTT con Mosquitto. Incluye un publicador y un suscriptor que se comunican a través de un broker MQTT para simular el comportamiento de un sensor de luz y un controlador de luces.

## Requisitos
Antes de ejecutar el proyecto, asegúrate de tener lo siguiente:

1. Ubuntu con interfaz gráfica.
2. Mosquitto instalado como broker MQTT


`sudo apt update`

`sudo apt install mosquitto mosquitto-clients`

3. Python 3 y el paquete paho-mqtt instalado:

`pip install paho-mqtt`

4. Clonar o descargar el conetenido del repositorio.


## Archivos

1. suscriptor.py: Código del suscriptor MQTT que utiliza el serividor mosquitto para recibe los mensajes del sensor de luz y simula el encendido o apagado de luces.

2. publicar_sensor.sh: Un archivo Shell Script que actúa como publicador MQTT y envía mensajes al broker con datos del sensor de luz.

## Ejecución
### 1. Iniciar el Broker MQTT
Comprobar que el broker Mosquitto esté en ejecución:

`sudo systemctl start mosquitto`

Verifica que el servicio esté activo:

`sudo systemctl status mosquitto`

### 2. Ejecutar el Suscriptor
Abre una terminal y ejecuta el script del suscriptor:

`python3 subs.py`

El suscriptor quedará a la espera de mensajes en el tema iot/sensor/luz.


### 3. Ejecutar el Publicador
En otra terminal, ejecuta el script Shell para publicar datos del sensor:

`./publicar_sensor.sh`

El publicador enviará mensajes con datos del sensor al tema iot/sensor/luz en intervalos regulares.

##Verificación
###Mensajes del Suscriptor:


Si el value del sensor es menor a 50 y accuracy es mayor a 0.9, el suscriptor mostrará:
Copiar código
Encendiendo las luces...
Si el value es mayor o igual a 50 o accuracy es menor o igual a 0.9, el suscriptor mostrará:
Copiar código
Apagando las luces...
Mensajes del Publicador:
### Ejemplo
#### Suscriptor 
![suscriptor](https://github.com/user-attachments/assets/183c2c0f-2d64-4080-807e-e8ad50082c3e)

#### Publicador
![Publicador](https://github.com/user-attachments/assets/05ef447a-d909-4228-96b0-68f31710fab3)



Puedes personalizar los datos que envía el publicador editando el JSON en el script publicar_sensor.sh.



## Personalización
Modificar los datos del sensor:
Edita el archivo publicar_sensor.sh y ajusta los valores en el JSON:

`json
{
    "device_id": "5ee9df89-a719-4e9a-ac54-84b9c3096f40",
    "event_time": "2024-11-19T15:00:00Z",
    "value": 45,
    "accuracy": 0.95
}
`
