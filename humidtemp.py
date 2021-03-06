#!/usr/bin/python
import json
import time
import requests
import board
import busio
import adafruit_am2320

# create the I2C shared bus
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_am2320.AM2320(i2c)

host = '192.168.43.228'


def postHumidity(value):
    print("Posting humidity to API")

    url = 'http://'+host+':8090/sensors/'
    payload = {
        'type': 'humidity',
        'value': value
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)


def postTemp(value):
    print("Posting temp to API")

    url = 'http://'+host+':8090/sensors/'
    payload = {
        'type': 'temp',
        'value': value
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)


starttime = time.time()
while True:
    print("Temperature: ", sensor.temperature)
    print("Humidity: ", sensor.relative_humidity)

    postHumidity(sensor.relative_humidity)
    postTemp(sensor.temperature)

    time.sleep(5.0 - ((time.time() - starttime) % 5.0))
