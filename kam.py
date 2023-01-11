import serial
import time


class KAM:
    def test1(self):
        ser = serial.Serial("COM5", 19200, timeout=1)  # Open named port
        # ser.baudrate = 19200  # Set baud rate to 9600
        ser.close()
        ser.open()
        ser.write(b"time\n\r")
        count = 2
        # temp_count = (count - 2)
        while count > 0:
            temp = ser.readlines()
            time.sleep(5)
            print(temp)
            count = count - 1
        time.sleep(10)

    def test2(self):
        ser = serial.Serial("COM5", 19200, timeout=1)  # Open named port
        # ser.baudrate = 19200  # Set baud rate to 9600
        ser.close()
        ser.open()
        ser.write(b"date\r\n")
        count = 2
        # temp_count = (count - 2)
        while count > 0:
            temp = ser.readlines()
            time.sleep(5)
            print(temp)
            count = count - 1
        time.sleep(10)

    def test3(self):
        ser = serial.Serial("COM5", 19200, timeout=1)  # Open named port
        # ser.baudrate = 19200  # Set baud rate to 9600
        ser.close()
        ser.open()
        ser.write(b"output\r\n")
        count = 2
        # temp_count = (count - 2)
        while count > 0:
            temp = ser.readlines()
            time.sleep(1)
            print(temp)
            count = count - 1
        time.sleep(30)

    def test4(self):
        ser = serial.Serial("COM5", 19200, timeout=1)  # Open named port
        # ser.baudrate = 19200  # Set baud rate to 9600
        ser.close()
        ser.open()
        ser.write(b"=alarm,80\n\r")
        count = 2
        # temp_count = (count - 2)
        while count > 0:
            temp = ser.readlines()
            time.sleep(1)
            print(temp)
            count = count - 1
        time.sleep(10)

    def test5(self):
        ser = serial.Serial("COM5", 19200, timeout=1)  # Open named port
        # ser.baudrate = 19200  # Set baud rate to 9600
        ser.close()
        ser.open()
        ser.write(b"output1\n\r")
        # ser.write(b"?modbus\r\n")
        count = 2
        # temp_count = (count - 2)
        while count > 0:
            temp = ser.readlines()
            time.sleep(1)
            print(temp)
            count = count - 1
        time.sleep(10)

    def test6(self):
        ser = serial.Serial("COM5", 19200, timeout=1)  # Open named port
        # ser.baudrate = 19200  # Set baud rate to 9600
        ser.close()
        ser.open()
        ser.write(b"=ostart\n\r")
        count = 2
        # temp_count = (count - 2)
        while count > 0:
            temp = ser.readlines()
            time.sleep(1)
            print(temp)
            count = count - 1
        time.sleep(10)

    def test7(self):
        ser = serial.Serial("COM5", 19200, timeout=1)  # Open named port
        # ser.baudrate = 19200  # Set baud rate to 9600
        ser.close()
        ser.open()
        ser.write(b"=ostop\n\r")
        count = 2
        # temp_count = (count - 2)
        while count > 0:
            temp = ser.readlines()
            time.sleep(1)
            print(temp)
            count = count - 1
        time.sleep(10)


if __name__ == "__main__":
    kam1 = KAM()
    kam1.test1()
    kam1.test2()
    kam1.test3()
    kam1.test4()
    kam1.test5()
    kam1.test6()
    kam1.test7()
