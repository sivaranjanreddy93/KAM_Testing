from itertools import chain

list0 = []
list1 = []


class sample1:
    def ram1(self):
        with open('lookup_table.txt') as f:

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
            for i in range(len(test_list)):
                if test_list[i] > 0 and test_list[i] < 101:
                    list1.append(0)
                else:
                    list1.append(1)
            print(list1)
            q = sum(list1)
            print(q)
            # if q == 0:
            #     return 0
            # else:
            #     return 1

if __name__ == "__main__":
    kam1=sample1()
    kam1.ram1()
