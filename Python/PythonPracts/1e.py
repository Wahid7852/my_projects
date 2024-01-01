def isPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
    

num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")

print("\nCheck if the string is Palindrome or not")
string = input("Enter a string: ")
if isPalindrome(string):
    print("The string is Palindrome")
else:
    print("The string is not Palindrome")
