#!/usr/bin/python
import sys

import Adafruit_DHT

def tempHumidity():

    humidity, temperature = Adafruit_DHT.read(Adafruit_DHT.AM2302, 4)
    temperature = temperature * 9/5.0 + 32

    if humidity is not None and temperature is not None:
        #return 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
        return temperature, humidity
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)

def temp():
    preformat = '{}'.format(print(tempHumidity['0']))
    return preformat

def humidity():
   # print(tempHumidity['1'])
    preformat = '{}'.format(print(tempHumidity['1']))
    #eturn tempHumidity['1']
    return preformat

# print(tempHumidity()[1])

