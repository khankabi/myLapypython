"""write a python script to find sum of a digit"""

def getSum(n):
    sum=0
    while(n!=0):
        rem=n%10
        sum=sum+rem
        """ sum=sum+(n%10) """
        n//=10
        """n=n//10"""
    return sum

print("Hello User")
no=int(input("Enter the Number : "))
print(getSum(no))
