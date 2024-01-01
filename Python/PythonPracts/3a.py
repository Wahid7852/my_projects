def isPangram(string):
    string = string.lower()
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in string:
            return False
    return True

string = input("Enter a string: ")
if isPangram(string):
    print("The string is a pangram")
else:
    print("The string is not a pangram")
