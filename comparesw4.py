import serial
import time
import functools
# import lookuptable
import collections
from itertools import chain
list0 = []
list1 = []
flat_ls = []
list2 = []
test_list = []
class lookup_table:
    def ram1(self):
        with open('lookuptable.txt') as f:

            contents = f.readlines()
            for i in contents:
                abc = i.split(",")
                list0.append(abc)
                #list1.append(abc[1].replace("\n",""))
            # print("Before: " + str(list0))
            list_1D = list(chain.from_iterable(list0))
            # print(list_1D)
            del list_1D[0]  # x value removed
            del list_1D[0]  # =tablac removed
            del list_1D[0]
            test_list = []

            print(list_1D)

            for i in list_1D:
                # i = float(i)  # converted float and after converted string
                test_list.append(i)

            # Printing modified list

            print("Modified list is : " + str(test_list))

    def test1(self):
        ser = serial.Serial("COM5")  # Open named port
        ser.baudrate = 19200  # Set baud rate to 9600
        ser.close()
        ser.open()

        ser.write(b"~tablewcSW4\n\r")  # we did send the command

        count = 30
        temp_count = (count - 1)
        while count > 0:
            temp = ser.readlines(1)
            print(temp)  # we are getting output line by line

            list1.append(temp)
            count = count - 1
        print(list1)  # we are getting output added  to list

        # flat_ls = []
        for i in list1:
            for j in i:
                flat_ls.append(j.strip())
        # all sublistes we added the single list
        # every element have \n we removed and added the list
        print(flat_ls)

        time.sleep(1)
        count = count - 1
        final_list = flat_ls
        list2 = list()
        for i in final_list:
            output = i.decode('utf-8')  # we removed bytes data
            output = (str(output))  # converted the string data type
            list2.append(output)
        print(list2)

        time.sleep(1)
        count = count - 1
        # time.sleep(1)
        #     print("Finish")
        # ser.write(b"=ostop\r\n")

if __name__ == "__main__":
    kam = lookup_table()
    kam.ram1()
    kam.test1()

    # if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, test_list, list2), True):

    #     print("The lists test_list and list2 are the same")
    # else:
    #     print("The lists test_list and list2 are not the same")


    # used sort method
    # test_list.sort()
    # list2.sort()
    # if test_list == list2:
    #     print ("The lists test_list and list2 are the same") 
    # else:
    #     print ("The lists test_list and list2 are not the same") 

    # set method 
    # a=set(test_list)
    # b=set(list2)
    # if a == b :
    #     print("lists test_list and list2 are equal")
    # else :
    #      print("lists test_list and list2 are not equal")

    # x = set(test_list)
    # y = set(list2)
    # if x == y:
    #   print(True)
    # else:
    #   print(False)


    def compareList(l1,l2):
        if(collections.Counter(l1) == collections.Counter(l2)):
            return "Equal"
        else:
            return "Non equal"
l1=test_list
l2=list2
print("First comparison",compareList(l1,l2))
