import serial
import time
import lookup_table
from itertools import chain
import codecs

list0 = []
list1 = []


class lookup_table:
    def ram1(self):
        with open('lookuptable.txt') as f:
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

        count = 30
        temp_count = (count - 1)
        while count > 0:

            temp = ser.readlines(1)
            print(temp)
            list1.append(temp)
            count=count-1
        print(list1)


        flat_ls = []
        for i in list1:
            for j in i:

                flat_ls.append(j)

        print(flat_ls)

        final_list = []

        for i in flat_ls :
               final_list.append(i.strip())
        print(final_list)



                # print("Modified list is : " + str(test_list))
        time.sleep(1)
        count = count - 1
        # time.sleep(1)
        #     print("Finish")
        # ser.write(b"=ostop\r\n")



if __name__ == "__main__":
    kam1 = lookup_table()
    kam1.ram1()
    kam1.test1()
    