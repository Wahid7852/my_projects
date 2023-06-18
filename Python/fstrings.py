# fstrings are string formats that are used to print variables in a string

name = "Wahid"
age = 19
welc = f"Hey my name is {name} and I am {age} years old"
print(welc)

# or like
# welc1 = f"Hey my name is {0} and I am {1} years old"
# print(welc1.format(name, age))

# we can also use it like this

price = 45.6789
txt = f"The price is {price:.2f} dollars and for two items:, {2 * price:.2f}"
print(txt)
