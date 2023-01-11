import serial
import time


class sample:
    def test1(self, a):
        ser = serial.Serial("COM5")  # Open named port
        ser.baudrate = 19200  # Set baud rate to 9600
        ser.close()
        ser.open()

        ser.write(b"~tablewcSW1\\r")

        count = 10
        temp_count = (count - 2)
        while count > 0:
            temp = ser.readlines(1)
            return temp
            try:
             temp = temp[0].decode("utf-8")
            except:a
            count = count - 1
            continue
            temp1 = list(temp.split(","))
            return temp1
        # print(type(temp1))
            time.sleep(1)
            count = count - 1
        # time.sleep(1)
        #     print("Finish")
        # ser.write(b"=ostop\r\n")


if __name__ == "__main__":
    kam1 = sample()
    kam1.test1()