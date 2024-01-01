# file has many modes,
# r == read, w == write
# a == append
# append is write but it woudlnt clear out the alr written text

# f.write("Hello Y'all")
# f.close

# with open('idk.txt', 'a') as f:
#     f.write("\n56,78,45")

# with open('io_readlines.txt','r') as f:
#     i = 0
#     while True:
#         i= i + 1
#         line = f.readline()
#         if not line:
#             break
#         m1 = int(line.split(",")[0])
#         m2 = int(line.split(",")[1])
#         m3 = int(line.split(",")[2])
#         print(f"Marks of Student {i} in English is {m1*2}")
#         print(f"Marks of Student {i} in Maths is {m2*3}")
#         print(f"Marks of Student {i} in Science is {m3*4}")    5
#         print(line)    
# writelines() to write lines

with open('io_SeekReadTell.txt','w') as f:
    f.write("How high are you?")
    # f.truncate(5)
    f.close

with open('io_SeekReadTell.txt','r') as f:
    f.seek(5)
    print(f.tell()) # tells which pos we seeked to currently 

    data = f.read()
    print(data)