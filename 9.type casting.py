#Note: every input in python is treated as string so it is necessary to change it into int or other data type according to your requirement
#char to int to long to float to double

#ambiguity
a="1"
b="2"
print(a+b)
#output : 12


#solution
a=1
b=2
print(a+b)
#output : 3

#typecasting : the conversion of one data type into another data type is known as typecasting.
#types : 1. implicit - done by compiler 2. explicit - done by user/programmer using functions
"""
functions:
int()
float()
str()
ord()
her()
oct()
tuple()
set()
list()
dict()
"""

#example
a= "1"
b= "2"
print(int(a)+int(b))



#but sting should be valid otherwise it would lead to error . example is below
a="1"
b="sonu"
print(int(a)+int(b))
"""
Traceback (most recent call last):
  File "c:\Users\HP\Desktop\PYTHON\9.type casting.py", line 43, in <module>
    print(int(a)+int(b))
                 ^^^^^^
ValueError: invalid literal for int() with base 10: 'sonu'
"""