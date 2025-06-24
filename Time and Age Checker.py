import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
hour=int(input("Enter hour: "))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning sir! ")
elif(hour>=12 and hour<17):
    print("Good afternoon sir!")
elif(hour>=17 and hour<0):
    print("Good night Sir! ")


import time
t=time.strftime("%H:%M:%S")
hour=int(time.strftime('%H'))
hour=int(input("Enter hour: "))
print(hour)

if(hour>=0 and hour<10):
    print("Enter your function")
else:
    print("Enter your age is 10")
