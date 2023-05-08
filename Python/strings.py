a = "python"
print(a)

b = "hi"
print(b[0])
print(b[1])

c = """ Python is one of the most demanded programming languages in the job market. Surprisingly, it is equally easy to learn and master  Python. This python tutorial for absolute beginners in Hindi series will focus on teaching you python concepts from the ground up. """
# prints each letter
for character in c:
    print(character)

# prints from given to desired index // string slicing
print(c[5:15])

print(len(c))

d = "!!!wahid!!!"
print(d[-4:-2])
print(d.upper())
print(d.lower())
print(d.rstrip("!"))
print(d.lstrip("!"))
print(d.replace("wahid", "Abdul Wahid"))
print(d.split("a"))
