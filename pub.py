import grovepi
import json
import math
import time
from grovepi import*
mqttBroker -"192.168.43.242"
client - mqtt.client ("TEMPERATURE SENSOR HUMIDITY")
client. connect (mqttBroker, 1883,60)
# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
sensor - 4
The Sensor goes on digital port 4.
time.sleep(1)
# temp_ humidity sensor_ type
# Grove Base Kit comes with the blue sensor.
blue - 0
The Blue colored sensor.
while True:
try:
[temp,humidity] = grovepi.dht (sensor,blue)
if math.isnan (temp) - False and math. isnan (humidity) - False:
sensor _data - ("temp":temp ,"humidity" : humidityl
client.publish ("TEMPERATURE _HUMIDITY", str (sensor_data))
print ("Just published " + str (temp) + " to topic TEMPERATURE _ HUMIDITY")
print ("Just published " + str (humidity) + " to topic TEMPERATURE HUMIDITY")
time.sleep(1)
except IOErrOr:
print ("Error")
