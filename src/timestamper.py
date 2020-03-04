import time

file_object = open("log-ground-truth.csv", "w") # Overwrite existing log file and append to it
file_object.write("Time ns, Temperature\n")

while True:
    temp = input("Input measured temperature in Celcius:\n")
    temp = str(temp).replace("b'", "").replace("\\r\\n'", "")
    
    out = str(time.time_ns()) + ", " + temp + "\n"
    file_object.write(out)
    print(out)