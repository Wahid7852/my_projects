import random

# initialize list
l = []
for i in range(30):
    l.append(random.randint(1,365))

l.sort()
print(l)

# check for duplicates
i,flag = 0

while(i<len(l)-1):
    if(l[i]==l[i+1]):
        print("Duplicate found! ", l[i], l[i+1])
        flag=1
        break
    i=i+1

if flag==0:
    print("No Duplicates found")