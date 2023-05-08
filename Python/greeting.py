import time
timestamp = int(time.strftime('%H'))
if 6 <= timestamp <= 12:
    print("Good Morning")
else:
    if 12 <= timestamp <= 15:
        print("Good afternoon")
    elif 15 <= timestamp <= 21:
        print("Good Evening")
    else:
        print("Good Night!")
