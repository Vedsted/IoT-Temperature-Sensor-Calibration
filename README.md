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