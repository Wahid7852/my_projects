import time
t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))

if(hour>=0 and hour<12):
    print("Good morning!")
elif(hour>=12 and hour<16):
    print("Good afternoon!")
elif(hour>=16 and hour<20):
    print("Good evening!")
else:
    print("Good night!")
print("The current time is", t)
