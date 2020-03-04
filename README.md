# Temperature Sensor Calibration
This repository contains a solution to a problem in the course *Software Engineering of Internet of Things*, University of Southern Denmark. The problem is described briefly below.



# Context
*Copy from Hand-in description*

- Given enough insulation the temperature of a large enough heated mass will follow a predictable path towards the temperature of the surroundings.
- The response curve (temperature -> value) of a thermistor is quite simple.

# Exercise
*Copy from Hand-in description*

Design an experiment to calibrate the thermistor attached to your board, and create an ontology for mapping a device to a calibration.


# Repository Structure
* src/temperature.py -> python application measureing the temperature and sending it over serial
* src/client.py -> python application reading from serial and writing to log.csv


# Running the solution
1. Push code to IOT device:
    ```
    python3 -m there push src/temperature.py /flash/main.py
    ```

1. Reboot IOT device by diconnecting and connecting again.

1. Run the client program.
    ```
    python3 src/client.py
    ```



# Hardware description

## Temperature sensor
Ref: http://ww1.microchip.com/downloads/en/DeviceDoc/20001942F.pdf

The temperature sensor used is of the type MCP9700-E/TO which is an Linear Active Thermistor from Microchip. This means that the microchip convert temperatures to analog voltage.

Temperature range E = -40C to +125C
Package TO = Plastic Small Outline Transistor, 3-lead

Temperature accuracy: T_Ambient = -40C to +125C with deviations Min = -4.0C, Typical = +-2C, Max = 6C

Temperature Coefficient = 10.0 mV/C
Output voltage (when T_Ambient = 0C) = 500 mV
Thermal resistance = 131.9 C/W


## PyCom (ESP32)
Measures the output from the temperature sensor.
The attenuation level on the ADC pin should be set to 11db to read voltage levels 0-3.9V.
The default attenuation levels are described here: https://esphome.io/components/sensor/adc.html#adc-esp32-attenuation


* 0db for a full-scale voltage of 1.1V (default)
* 2.5db for a full-scale voltage of 1.5V
* 6db for a full-scale voltage of 2.2V
* 11db for a full-scale voltage of 3.9V

The following formula can be used to calculate the correct attenuation level for our application. We know that the temperature sensor outputs between 0-1750mV.

We know the formula to calculate dB given V_out and V_in, where V_in = 1100mV (it is the default value for the ESP32 ADC, but can vary between 1000-1200mV, and thus has to be measured and calibrated).

dB = 20 * log^(V_out/V_in)

Rewriting the formula gives:

V_out = 10^(dB/20) * V_in

The V_out should contain the output voltage range of the temperature sensor which is 0-1750mV. Therefore, the dB we need for this application is dB = 6, which gives V_out = 2000mV (contains 1750mV).


# Experiment initial settings
Room temperature: 21.5 C
Initial water temp: 77.5 C
Water capacity: 0.8 l
