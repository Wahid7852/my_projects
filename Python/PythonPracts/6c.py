def read_last_lines(file_name, n):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        print(''.join(lines[-n:]))

n  = int(input('Enter the number of lines to read: '))
file_name = input('Enter the file name: ')
read_last_lines(file_name, n)

