from ostart import *
import time
class kammodify1:
    def test(self,a):
        ser = serial.Serial("COM7")  # Open named port
        ser.baudrate = 19200  # Set baud rate to 9600
        ser.write(b"=date,<10/29/2022>\r\n")

        count = 10
        temp_count = (count - 2)
        while count > 0:
            # temp = [b'54.100,12.656,*,3.1748,0.000,11.203,*,2.5051,-5.135,93.988,-428.772,*,9.716,OC,S3,*5CAB\r\n']

            temp = ser.readlines()
            return temp
            #print(type(temp))  # [b'54.100,12.656,*,3.1748,0.000,11.203,*,2.5051,-5.135,93.988,-428.772,*,9.716,OC,S3,*5CAB\r\n']
            # temp=[b'54.100,12.656,*,3.1748,0.000,11.203,*,2.5051,-5.135,93.988,-428.772,*,9.716,OC,S3,*5CAB\r\n']
            try:
                   temp = temp[0].decode(
                        "utf-8")  # [b'49.883,11.981,*,3.1815,0.000,11.203,*,2.5232,-4.186,88.137,-428.A?\xa6\xe4*,9.793,OC,S3Percent Water,4-20mA Output,*,S1 Voltage,WC Offset,Temp Comp Factor,*,S2 Voltage,OC Offset,Board Temp,Probe Temp,*,S3 Voltage,Fluid Phase,Fluid Phase Sensor,CRC\r\n']
            except:
                    count = count - 1
                    return
                    temp1 = list(temp.split(","))
                    return temp1
         # print(type(temp1))

        time.sleep(1)
        count = count - 1
        #time.sleep(1)
        #print("Finish")
        ser.write(b"=date,<10/29/2022>\r\n")

if __name__ == "__main__":
    kam2=kammodify1()
    kam2.test()
