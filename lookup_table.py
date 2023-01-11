import serial
import time


class lookup_table:
    def test1(self):
        ser = serial.Serial("COM5")  # Open named port
        ser.baudrate = 19200  # Set baud rate to 9600
        ser.close()
        ser.open()

        ser.write(b"~tablewcSW4\n\r")

        count = 30
        temp_count = (count - 2)
        while count > 0:
            temp = ser.readlines(1)
            print(temp)

            # try:
            #     temp = temp[0].decode(
            #         "utf-8")
            # except:
            #     count = count - 1
            #     continue
            #     temp1 = list(temp.split(","))
            #     return temp1
        # print(type(temp1))
        time.sleep(1)
        count = count - 1
        # time.sleep(1)
        #     print("Finish")
        # ser.write(b"=ostop\r\n")


if __name__ == "__main__":
    kam1 = lookup_table()
    kam1.test1()