import ssl
import sys
import json

import paho.mqtt.client

def on_connect(client, userdata, flags, rc):
	print('connected (%s)' % client._client_id)
	client.subscribe(topic='iot/sensor/luz', qos=2)

def on_message(client, userdata, message):
	print('------------------------------')
	print('Tema: %s' % message.topic)
	print('Payload recibido: %s' % message.payload.decode('utf-8'))

	try:
		data = json.loads(message.payload.decode('utf-8'))
		value = data.get('value',0)
		accuracy = data.get('accuracy',0)

		if value < 50 and accuracy >0.9:
			print('El sensor indica poca luz. Las luces serán ENCENDIDAS.')
		else:
			print('Las luces serán Apagadas.')
	except json.JSONDecodeError:
		print('Error: El payload no esta en formato JSON.')


def main():
	client = paho.mqtt.client.Client(client_id='diego-subs', clean_session=False)
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(host='127.0.0.1', port=1883)
	client.loop_forever()

if __name__ == '__main__':
	main()

sys.exit(0)
