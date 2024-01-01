def histogram(numbers):
    for num in numbers:
        print('*' * num)

user_input = input("Enter a list of integers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]
histogram(numbers)
