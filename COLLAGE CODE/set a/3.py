""" write a python script to check whether a number is perfect or not, aesa number jiske dinominator ka sum karne pe vahi number aayega"""

def find_perfect(n):
    sum=0    
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    return sum
    
print("Hello User")
n=int(input("Enter the Number : "))
result=find_perfect(n)
if(n==result):
    print(f"{n} is perfect")
else:
    print(f"{n} is Not Perfect")

  
