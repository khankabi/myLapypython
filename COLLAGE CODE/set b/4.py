""" Write a program which accept an integer value as "n" and display all prime numbers till "n" """
def isPrime(n):
    prime = 0
    if(n==1 or n==0):
        return False
    for i in range(2,n):
        if(n%i ==0):
            return False
    return True
   
n=int(input("Enter a Number : "))
for i in range(n):
    if(isPrime(i)):
        print(i,end = " ")


