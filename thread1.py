import serial
from threading import Thread
import time
import thread

import ostart

# function to create threads
def threaded_function(arg):
    kam=("=ostart", "output", "~tablewcSW2", "?tcfoc", "?tcfwc", "time")
    for x in kam:
        print(x)
       # wait 1 sec in between each thread
        sleep(5)

def test_function(a, b, c, d, e, f, g, h):
        ser = serial.Serial("COM11")  # Open named port
        ser.baudrate = 19200  # Set baud rate to 9600
        for x in ["=ostart", "output", "~tablewcSW3", "?tcfoc", "?tcfwc", "time"]:
            time.sleep(30)
            ser.write(b"=x \r\n")

            count = 10
            temp_count = (count - 2)
        while count > 0:
            try:
                temp = temp[0].decode(
                    "utf-8")  # [b'49.883,11.981,*,3.1815,0.000,11.203,*,2.5232,-4.186,88.137,-428.A?\xa6\xe4*,9.793,OC,S3Percent Water,4-20mA Output,*,S1 Voltage,WC Offset,Temp Comp Factor,*,S2 Voltage,OC Offset,Board Temp,Probe Temp,*,S3 Voltage,Fluid Phase,Fluid Phase Sensor,CRC\r\n']
            except:
                count = count - 1
                temp = list(temp.split(","))
                temp = ser.readlines()
                return temp

if __name__ == "__main__":
    thread1 = Thread(target=threaded_function, args=(7,))
    st = threaded_function().Thread(target=test_function, args=("=ostart", "output", "~tablewcSW3", "?tcfoc", "?tcfwc", "time"))
    thread.start()
    thread.join()
    print("thread finished...exiting")
