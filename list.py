import serial
import time
from time import sleep


class serialostop:
    def thread(self):
        ser = serial.Serial("COM4", 19200, timeout=1)  # Open named port
        ser.close()
        ser.open()
        # ser.baudrate = 19200  # Set baud rate to 9600
        ser.write = [b"=ostart1\n\r", "output\n\r", "~tablewcSW2\n\r"]
        count = 2
        temp_count = (count - 2)
        while count > 0:
            temp = ser.readlines()
            print(temp)
            try:
                temp = temp[1].decode("utf-8") #[b'49.883,11.981,*,3.1815,0.000,11.203,*,2.5232,-4.186,88.137,-428.A?\xa6\xe4*,9.793,OC,S3Percent Water,4-20mA Output,*,S1 Voltage,WC Offset,Temp Comp Factor,*,S2 Voltage,OC Offset,Board Temp,Probe Temp,*,S3 Voltage,Fluid Phase,Fluid Phase Sensor,CRC\r\n']
            except:
                count = count - 2
                continue
            temp1 = list(temp.split(","))
            print(temp1)

        # print(type(temp1))
        # time.sleep(1)
        count = count - 2
        time.sleep(5)
        print("Finish")
        ser.close()


if __name__ == "__main__":
      kam1 = serialostop()
     # kam1.thread()
