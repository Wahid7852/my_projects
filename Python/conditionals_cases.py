# if elif else
num = 1  # int(input("Input a number: "))
if num < 0:
    print("Number is negative")
elif num == 0:
    print("Number is 0")
else:
    print("Number is positive")

# switch / match case, not works with python 3.8
# x = int(input("Enter a number: "))
# match x:
#     case 0:
#         print("X is 0")
#     case 1:
#         print("X is 1")
#     case _ if x!=10:
#         print("X is not 10")
#     case _ if x!=5:
#        print("X is not 5")
#     case _:
#         print(x)

# for loop
colors = ["red, green, blue"]
for color in colors:
    print(color)
    if color == "red, green, blue":
        print("rgb")
    for i in color:
        print(i)

# range(from, till, diff)
for k in range(1, 10, 2):
    print("\n", k + 1)

# while loop
count = 5
while count > 0:
    print(count)
    count = count - 1
else:
    print("Inside else")

# do...while
# count = count - 1

# continue...break
print("\n")
for i in range(1, 11):
    if i == 9:
        break
    if i == 6:
        print("Skipped")
        continue
    print("5 X ", i, "=", 5 * i)
