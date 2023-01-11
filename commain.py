import serial
import time
import lookup_table
from itertools import chain

list0 = []
list1 = []
list2 = []


class lookup_table:
    def ram1(self):
        with open('lookuptablesw4.txt') as f:
            contents = f.readlines()
            for i in contents:
                abc = i.split(",")
                list0.append(abc)
                # list1.append(abc[1].replace("\n",""))
            # print("Before: " + str(list0))
            list_1D = list(chain.from_iterable(list0))
            # print(list_1D)
            del list_1D[0]
            del list_1D[0]
            del list_1D[0]

            print(list_1D)
            test_list = [float(i) for i in list_1D]

            # Printing modified list
            print("Modified list is : " + str(test_list))
            # for i in range(len(test_list)):
            #     if test_list[i] > 0 and test_list[i] < 101:
            #         list1.append(0)
            #     else:
            #         list1.append(1)
            # print(list1)
            # q=sum(list1)
            # print(q)
            # if q==0:
            #     return 0
            # else:
            #     return 1

    def test1(self):
        ser = serial.Serial("COM5")  # Open named port
        ser.baudrate = 19200  # Set baud rate to 9600
        ser.close()
        ser.open()

        ser.write(b"~tablewcSW4\n\r")

        with open('') as f1:
          contents = f1.readlines()
        for i in contents:
            abc = i.split(",")
            list2.append(abc)
            list2.append(abc[1].replace("\n",""))
            print("Before: " + str(list2))
            list_2 = list(chain.from_iterable(list2))
            print("Modified list is : " + str())
        count = 10
        temp_count = (count - 2)
        while count > 0:
            temp = ser.readlines(1)
            print(temp)

            try:
                temp = temp[0].decode(
                    "utf-8")
            except:
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
    kam1 = lookup_table()
    kam1.ram1()
    kam1.test1()