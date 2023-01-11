import sample
import sample1


def compare(sample,sample1):
    with open(sample,'r') as f:
        d=set(f.readlines())


    with open(sample1,'r') as f:
        e=set(f.readlines())

    open('hi.txt','w').close() #Create the file

    with open('hi.txt','a') as f:
        for line in list(d-e):
           f.write(line)