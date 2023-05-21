# A basic list
# a list starts from 0 like array
# it can store strings and bools too
# marks = [2, 3, 4, "harry", True]

marks = [2, 3, 4, "wahid"]
print(marks[0])
print(type(marks))

# negative indexing
# it starts from -1 and from the right
print(marks[-2])

# converting negative index to positive
print(marks[len(marks)-2])

if 4 in marks:
    print("yes")
elif "hi" in "wahid":
    print("Yes")
else:
    print("No")

# list slicing
print(marks[1:3])

# can use i*i or i/i too
# lst = [i for i in range(4)]

# now add conditions like only odd / even
lst = [i for i in range(4) if i%2==0]
print(lst)