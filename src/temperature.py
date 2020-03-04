import pycom
from machine import UART, Pin, ADC
import time

# Disables the LED heartbeat
#pycom.heartbeat(False)+

# Get data from lopy4 pins
# https://docs.pycom.io/gitbook/assets/lopy4-pinout.pdf
# https://docs.pycom.io/datasheets/development/lopy4/#pinout

uart = UART(0)
uart.init(115200, bits=8, parity=None, stop=1)

#p_blue = Pin('P16')
#p_red = Pin('P19')

adc = ADC()
blue_pin = adc.channel(pin='P16') # Data pin

p_red = Pin('P19', mode=Pin.OUT)
p_red.value(1)

while True:
    val = blue_pin()
    print(val)
    time.sleep(1)