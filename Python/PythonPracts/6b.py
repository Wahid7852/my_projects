def append_text(file_name, text):
    with open(file_name, 'w') as f:
        f.write(text)
        f.close()

with open('test.txt') as f:
    print(f.read())

append_text('test.txt', '\nThis is a new line.')
