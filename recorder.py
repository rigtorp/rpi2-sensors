#!/usr/bin/python

import sqlite3
import datetime
import Adafruit_BMP.BMP085 as BMP085
import Adafruit_DHT

conn = sqlite3.connect('sensors.db')
conn.execute('''CREATE TABLE IF NOT EXISTS 
    measurements (ts DATETIME NOT NULL, 
    sensor TEXT NOT NULL, 
    value DOUBLE NOT NULL, 
    PRIMARY KEY (ts, sensor))''')

sensor = BMP085.BMP085()
bmp085_temp = sensor.read_temperature()
bmp085_pressure = sensor.read_pressure()
dht11_indoor_humidity, dht11_indoor_temp = Adafruit_DHT.read_retry(11, 17)
dht11_outdoor_humidity, dht11_outdoor_temp = Adafruit_DHT.read_retry(11, 22)

#print bmp085_temp, bmp085_pressure
#print dht11_indoor_humidity, dht11_indoor_temp
#print dht11_outdoor_humidity, dht11_outdoor_temp

ts = datetime.datetime.utcnow()
conn.execute('''INSERT INTO measurements VALUES (?, ?, ?)''', (ts, 'bt', bmp085_temp))
conn.execute('''INSERT INTO measurements VALUES (?, ?, ?)''', (ts, 'bp', bmp085_pressure))
conn.execute('''INSERT INTO measurements VALUES (?, ?, ?)''', (ts, 'it', dht11_indoor_temp))
conn.execute('''INSERT INTO measurements VALUES (?, ?, ?)''', (ts, 'ih', dht11_indoor_humidity))
conn.execute('''INSERT INTO measurements VALUES (?, ?, ?)''', (ts, 'ot', dht11_outdoor_temp))
conn.execute('''INSERT INTO measurements VALUES (?, ?, ?)''', (ts, 'oh', dht11_outdoor_humidity))
conn.commit()
