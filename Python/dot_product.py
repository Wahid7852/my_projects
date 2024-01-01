import random

l = []
x = []

for i in range(100):
    l.append(random.randint(1,10))
    x.append(random.randint(1,10))

sum = 0
for i in range(len(l)):
    sum = sum + l[i]*x[i]
print(sum)