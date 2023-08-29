
"""
__name__ :
ye ek esa variable hai jo identify karega whether function actual file pe run ho rahe hai ya
import file me run ho rahe hai
matlab k
agar sonu.py me koi function hai suppose welcome( ) function hai jo call bhi ho raha hai
or sonu.py ko agar me aman.py me import kru or welcome() ko call kru to result do bar execute ho jayaga
kyuki sonu.py me bhi  me welcome() ko call kar raha tha

ye complex programming me use hone wali chiz hai

example 1 ko refer  karo problem k liye
"""


import myownmodule as mod #just reference k liye as keyword use kar raha hu , completely optinal hai
# print(__name__)
# mod.welcome()
#output witthout __name__ concept
# hello guys
# hello guys

#output with __name__ concept
# __main__
# hello guys
# myownmodule




#some randome try
# print(__file__)
# output
# c:\Users\HP\Desktop\PYTHON\45. if __name__.py



# print(__doc__)
#puri comment jo mene uper likhi hai , doc string boltey isko

print(__package__)
print(__annotations__)
print(__builtins__)
print(__cached__)
print(__loader__)
print(__package__)
print(__spec__)
print(__import__)
print(__build_class__)
