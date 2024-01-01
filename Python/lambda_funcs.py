# lambda funcs are pretty much a function defn but compressed
# useful for multiple simple oneline funcs

# for eg: 
# def sum(a,b):
#     return a + b

# print(sum(5,6))
# can be written as

sum = lambda a,b: a+b
print(sum(5,6))

# lets create a function which will take a fn as value,
# lambda funcs can be created to be used as anon. funcs and can be assigned as a func into another func

def MulPlus2(fx, value):
    return 2 + fx(value)
print(MulPlus2(lambda x: x*x, 2))