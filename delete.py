import serial
import threading
import time


#class serialostop:
l=["=ostart", "output", "~tablewcSW3", "?tcfoc", "?tcfwc", "time"]
def kam1():
        print(' \n first_thread started')
        ser = serial.Serial("COM7")  # Open named port
        ser.baudrate = 19200  # Set baud rate to 9600

def kam2():
        print(' \n second_thread started')
        ser = serial.Serial("COM7")  # Open named port
        ser.baudrate = 19200  # Set baud rate to 9600

        time.sleep(30)
        ser.write(b"=x\r\n")
        count = 10
        temp_count = (count - 2)
        temp=[]
        while count > 0:
                # temp = [b'54.100,12.656,*,3.1748,0.000,11.203,*,2.5051,-5.135,93.988,-428.772,*,9.716,OC,S3,*5CAB\r\n']
                try:
                    temp = temp[0].decode("utf-8")  # [b'49.883,11.981,*,3.1815,0.000,11.203,*,2.5232,-4.186,88.137,-428.A?\xa6\xe4*,9.793,OC,S3Percent Water,4-20mA Output,*,S1 Voltage,WC Offset,Temp Comp Factor,*,S2 Voltage,OC Offset,Board Temp,Probe Temp,*,S3 Voltage,Fluid Phase,Fluid Phase Sensor,CRC\r\n']
                except:
                    count = count - 1
                    temp = list(temp.split(","))
                    temp = ser.readlines()
                    return temp

            # print(type(temp))  # [b'54.100,12.656,*,3.1748,0.000,11.203,*,2.5051,-5.135,93.988,-428.772,*,9.716,OC,S3,*5CAB\r\n']
            # temp=[b'54.100,12.656,*,3.1748,0.000,11.203,*,2.5051,-5.135,93.988,-428.772,*,9.716,OC,S3,*5CAB\r\n']



ft = threading.Thread(target=kam1())
st = threading.Thread(target=kam2())

ft.start()
st.start()
st.join()
print(' \n X ', time.ctime())