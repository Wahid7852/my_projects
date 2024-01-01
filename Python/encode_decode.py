import random

def encode(word):
    if len(word) >= 3:
        word = word[1:] + word[0]
        word = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 3)) + word + ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 3))
    else:
        word = word[::-1]
    return word

def decode(word):
    if len(word) >= 3:
        word = word[3:-3]
        word = word[-1] + word[:-1]
    else:
        word = word[::-1]
    return word

word = input("Enter a word: ")
choice = input("Do you want to encode or decode? (e/d): ")
if choice == 'e':
    print("Encoded word: ", encode(word))
elif choice == 'd':
    print("Decoded word: ", decode(word))
else:
    print("Invalid choice")