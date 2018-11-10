from datetime import datetime
from time import sleep
import serial

file = open("log.txt", "w")
string = "hello World"

while True:
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file.write(time + "\n")
    sleep(1)
