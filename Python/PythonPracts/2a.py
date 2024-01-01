def isVowel(char):
    if char in "aeiouAEIOU":
        return True
    else:
        return False
    
char = input("Enter a character: ")
if isVowel(char):
    print("The character is a vowel")
else:
    print("The character is not a vowel")