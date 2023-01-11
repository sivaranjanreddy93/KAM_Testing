import serial
import time
from time import sleep

class serialostop1:
 ser = serial.Serial("COM4")
 ser = serial.Serial(port='/dev/ttyUSB0',baudrate=19200)


 def threaded_function(arg):

    ser = serial.Serial("COM4")  # Open named port
    ser.baudrate = 19200  # Set baud rate to 9600
    x = ("=ostart", "output", "~tablewcSW2", "?tcfoc", "?tcfwc", "time")
    time.sleep(30)
    ser.write(b"=x\r\n")
    count = 10
    temp_count: int = (count - 2)
    temp = []
while 1:
    for line in serialostop1.read(1):
        input+=chr(line)

        if input=='=ostart':
            for x in range (1 ,10):  # this is the loop i want to break
                print(x)
                sleep(5)
        if input=='output':
            for x in range (1 , 10):  # this is the loop i want to break
                print(x)
                sleep(5)

        if input=='~tablewcSW2':
            print('K received -> BREAK')
            break
# print("Finished")

# if __name__ == "__main__":
#     kam2=kammodify1()
#     kam2.test()
