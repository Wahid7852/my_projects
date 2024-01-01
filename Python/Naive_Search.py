import random

l = []
for i in range(100000):
    l.append(random.randint(1,99999))

a = 0
while (a!=-1):
    print("Hey, enter element to check or type -1 to exit: ")
    a = int(input())
    flag = 0
    for i in range(len(l)):
        if (a==l[i]):
            print("Present in list")
            flag=1
            break
        
        if flag==0:
            print("Not Present in list")