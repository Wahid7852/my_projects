# tradition way:
def cube(x):
    return x*x*x

l = [2,3,4,5,6,8,2] 

# newL = []
# for items in l:
#     newL.append(cube(items))
# print(newL)

newL = list(map(cube, l))
print(newL)