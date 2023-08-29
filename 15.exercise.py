import time
print("hello guys")
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
hour=int(time.strftime("%H"))
minute=int(time.strftime("%M"))
second=int(time.strftime("%S"))
print("Hour:",hour)
print("minute:",minute)
print("second:",second)



#write a python program to display greeting message according to current timestamp
# i import a time module to use time properties
# solution:
if(hour>=1 and hour<=12):
    print("good morning")
elif(hour>=12 and hour<=16):
    print("good afternoon")
elif(hour>=16 and hour<=24):
    print("good evening")
else:
    print("good night")
print("thank you")
