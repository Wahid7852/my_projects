import random

# l = []
# x = []

# for i in range(100):
#     l.append(random.randint(1,100))

# while(len(l)>0):
#     min = l[0]
#     for i in range(len(l)):
#         if l[i] <  min:
#             min=l[i]
#     x.append(min)
#     l.remove(min)
    
# print(l)
# print(x)

def gen_list(l):
    for i in range(10):
        l.append(random.randint(1,100))
    return l

def obv_sort(l):
    x = []
    while len(l)>0:
        min = l[0]
        for i in range(len(l)):
            if l[i] < min:
                min = l[i]
        x.append(min)
        l.remove(min)
    return x

l=[]
print(gen_list(l))
print(obv_sort)