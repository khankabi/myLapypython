""" import is very important feature of python used to import module
syntax :
import module_name
necessary to write class name
refer example 1

from keyword is used to import specific object from module
here i imported sqrt pi and floor function from math class
note: whenever spectificaly import something then no need to write class name before using function
refer example 2

* is used to import everything from module
no need to write class name
refer example 3



#as keyword
reference to module name
syntax
import module_name as small_name
refer example 4


#dir() function is used to retrieve items from module
syntax
print(dir(module_name))
refer example 5


#my own module
refer example 6
"""
#exmaple1W
# import math
# print(math.sqrt(25))



#example 2
# from math import sqrt,pi,floor
# print(floor(sqrt(25)*pi))


#example 3
# from math import *
# # print(math.sqrt(25))
# print(floor(sqrt(25)*pi))
# print("it is nor recommanded to import everything")


#example 4
# import math as m
# # print(math.sqrt(25))
# print(m.sqrt(25))


#example 5
# import math
# lst=dir(math)
# for  index,i in enumerate( lst):
#     print(index,i)


#example 6
#my own module : reference name is optional
import myownmodule as mod
print(dir(mod))
mod.welcome()
