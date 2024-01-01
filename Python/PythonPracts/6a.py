def read_file(file_name):
    with open(file_name, 'r') as f:
        print(f.read())
        
read_file('test.txt')
