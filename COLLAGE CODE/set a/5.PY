"""WRITE A PYTHON PROGRAM TO CHECK WHETHER A INPUT NUMBER IS PALINDROM OR NOT"""
num=int(input("Enter a Number:"))
temp=num
 
def palindrom(temp):
    rev=0
    rem=0
    while(temp>0):
        rem=temp%10
        rev=rev*10+rem
        temp=temp//10
    if(rev==num):
        print(f"{rev} is palindrom")
    else:
        print(f"{num} is not palindrom" )
# palindrom(temp)

print("{} is ".format(num))
 
  
