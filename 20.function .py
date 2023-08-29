#without return statement
"""
def calculategmean(a,b):
    geometric_mean=(a*b)/(a+b)
    print(geometric_mean)
a=9
b=8
calculategmean(a,b)
"""




"""
print("\n\n\n")
# with return statement
def calculategmean(a,b):
    geometric_mean=(a*b)/(a+b)
    return geometric_mean
a=9
b=8
print(calculategmean(a,b))
"""




"""
print("\n\n\n")
#write a python program to find maximum number using function
def findmax(a,b):
    if(a>b):
        return a
    elif(b>a):
        return b
    else:
        # print("wrong input") #this will return none (try this one time)
        return "wrong input"
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print(findmax(num1,num2))
"""



"""
#how declare function ( not define ) : pass is a keyword to declare function in python
def declared_function():
    pass
"""

#built-in function
print(max(12,32))
print(min(12,32))


#return :  the return is used to return the value of the expression back to the calling function
#note: only first return statement is considered other will ignore
