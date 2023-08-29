"""
short hand is very use full for small operations
syntax
variable = value if condition else statement
or
some operation based on certain condition
"""

#example
a = 330
b = 3303
print("A") if a>b else print("=") if a==b else print("B")

#example 2
c= 9 if a>b else 0
print(c)

#example 3
m=0
name="sonu" if m!=0 else "shaikh"
print(name)