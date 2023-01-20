from machine import Pin, I2C
#Library https://github.com/robert-hh/BMP085_BMP180
from bmp085 import BMP180
import time
import utime

#Global Variable
ledTick = 0
bmp180Tick = 0

start_time = time.ticks_ms()

def millis():
    return time.ticks_ms() - start_time


print('Version: Read Data from BMP180 sensor and display on shell')

#setup Digital O/p
led = Pin(2, Pin.OUT)

#setup i2c devices
i2c = I2C(scl=Pin(22), sda=Pin(21))
bmp = BMP180(i2c)
bmp.oversample = 2
#https://meteologix.com/my/observations/pressure-qnh.html
#At Arau, approx. 20m above sealevel ~ 1011 hPa 
bmp.sealevel = 1011 

while True:    
    if millis() >= ledTick:
        ledTick = millis()+1000
        led.value(not led.value())

    if millis() >= bmp180Tick:
        bmp180Tick = millis() + 10000
        temp = bmp.temperature
        pressure = bmp.pressure
        altitude = bmp.altitude
        
        timestamp = utime.time()
        time_tuple = utime.localtime(timestamp)
        time_string = "{}-{:02d}-{:02d} {}:{}:{}".format(time_tuple[0],time_tuple[1],time_tuple[2],time_tuple[3],time_tuple[4],time_tuple[5])
        print(time_string)
        
        data_sensor_string = "T:{:.2f} °C, P:{:.2f} hPa, Alt:{:.2f} meter".format(temp,pressure,altitude)
        print(data_sensor_string)
