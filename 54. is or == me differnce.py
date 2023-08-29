"""
is and == both are comparison operators
is - compare exect location of object in memory
== - compare values
"""

a=4
b="4"
print(a is b) # exact location of object in memory
print(a == b) #value


a=[1,2,3,45]
b=[1,2,3,45]
print(a is b) #location in memory , dono ek hi hai ya nahi
print(a == b) #compares value , dono ki value same hai ya nahi


a=3
b=3
print(a is b)
print(a == b)

a= None
b=None
print(a is None)
print(b is None)
print(a is b)
print(a == b)