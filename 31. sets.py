"""
SET - is a collection of well defined objects
it cannot contain duplicate item and also it is unchangble
enclosed by curly brackets
"""
s={2,10,4,2,26,6}
print(s)
print(type(s))

print("\n\n\n")
info={"sonu",18,"male",7.8}
print(info)
print(type(info))


print("\n\n\n")
#how to make empty set
harry= set() # rather than harry={}
print(harry)
print(type(harry))


print("\n\n\n")
#accessing item of set
for value in info:
    print(value)