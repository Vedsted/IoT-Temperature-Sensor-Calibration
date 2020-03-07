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

blue_pin = adc.channel(pin='P16', attn=2) # Data pin (V_out pin on Thermistor), attn is the attenuation level
                                            # If attn=0, then the reading of the pin will be too high. attn=3 will lower the reading to the expected output from the thermistor.

p_red = Pin('P19', mode=Pin.OUT) # Use this pin to feed voltage to the Thermistor (V_dd pin on the Thermistor)
p_red.value(1) # Set the pin to HIGH i.e. output a current to the Thermistor

while True:
    val = blue_pin()
    print(val)
    time.sleep(1)