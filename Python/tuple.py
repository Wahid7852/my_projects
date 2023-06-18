# tup = (1)
# print(type(tup))
# gives output as int as the compiler gets confused that is the list tuple or int
# to solve this, add a ',' after 1 or x
tup = (1, 2, 43, 12, "green", True)
print(type(tup))

# tuples need (), lists are [] and tuples cannot be edited by append or other sorts of list methods
# tuples are like static lists

if 32 in tup:
    print("yes 32 exits")

# tuple slicing
tup2 = tup[1:4]
print(tup2)

res = len(tup)
res1 = tup.count(3)
res2 = tup.index(3)
res3 = tup.index(3, 4, 6)
print(res, res1, res2, res3)
