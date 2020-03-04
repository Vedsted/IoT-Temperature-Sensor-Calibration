import serial
import threading
import time

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)


file_object = open("log.csv", "w") # Overwrite existing log file and append to it
file_object.write("Time ns, Temperature\n")

while True:
    temp = ser.readline() # Blocking until line is received
    temp = str(temp).replace("b'", "").replace("\\r\\n'", "")
    
    out = str(time.time_ns()) + ", " + temp + "\n"
    file_object.write(out)
    print(out)
