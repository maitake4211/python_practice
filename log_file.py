from datetime import datetime
from time import sleep
import serial

# file = open("log.txt", "w")
string = "hello World"


while True:
    ser = serial.Serial('COM18',9600,timeout=10)
    # time = datetime.now().strftime("%Y%m%d%H%M%S")
    data = ser.readline()
    # file.write(time)
    # file.write(":")
    #file.write(str_data)
    print(type(data))


ser.clone()
# file.close()
