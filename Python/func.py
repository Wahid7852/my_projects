def calcMean(a, b):
    mean = (a * b) / (a + b)
    print(mean)


def isGreater(a, b):
    if a > b:
        print("1st number is greater")
    else:
        print("2nd number is greater")

c,d = 2,1
# isGreater(c, d)
# calcMean(c, d)

e,f = 55,6
# isGreater(e, f)
# calcMean(e, f)

# return and avg
# one way to do an avg function:
# def average(ss, df):
#     print("average is", (ss + df) / 2)
#
#
# average(10, 23)

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        return sum/numbers

# e = average(5, 6, 7, 1)
# print(e)

# add enumeration to function
marks = [55, 66, 77, 88, 99]
for index, mark in enumerate(marks):
    print(index, mark)
    if (index == 2):
        print("I've scored 77 marks")