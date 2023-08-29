""" write a python script to check whether a input number is armstrong or not"""
def find_arm(n):
    temp = n
    sum=0
    while(temp!=0):
        rem=temp%10
        sum=sum+(rem*rem*rem)
        temp=temp//10
    if(n==sum):
        print(f"{n} is Armstrong")
    else:
        print(f"{n} is Not ArmStrong")
        
print("Hello User")
num=int(input("Enter the Number : "))
find_arm(num)

