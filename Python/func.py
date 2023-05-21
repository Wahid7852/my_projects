def calcMean(a, b):
    mean = (a * b) / (a + b)
    print(mean)


def isGreater(a, b):
    if a > b:
        print("1st number is greater")
    else:
        print("2nd number is greater")


c = 1
d = 2
isGreater(c, d)
calcMean(c, d)

e = 55
f = 6
isGreater(e, f)
calcMean(e, f)


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


e = average(5, 6, 7, 1)
print(e)
