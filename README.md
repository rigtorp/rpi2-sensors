# Raspberry Pi 2 Sensors

An expansion board for the Raspberry Pi 2 that measures temperature, humidity
and barometric pressure.

I used two DHT11 sensors, one for outdoor and one for indoor measurements of to
temperature and humidity. Barometric pressure is measured using a BMP085 sensor.

There is no schematic. The circuit is very simple: DHT11 sensors are fed 3.3V
and connected to GPIO pins 17 and 22 (4.7kOhm pullup, use whatever gives you
acceptable rise time). BMP085 sensor is fed 3.3V and connected to the I2C
interface.

![Image of circuit board front](https://github.com/rigtorp/rpi2-sensors/blob/master/front.jpg)
![Image of circuit board back](https://github.com/rigtorp/rpi2-sensors/blob/master/back.jpg)
