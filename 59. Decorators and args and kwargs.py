"""
Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:
@decorator_function
def my_function():
    pass

The @decorator_function notation is just a shorthand for the following code:

def my_function():
    pass
my_function = decorator_function(my_function)


Decorators are often used to add functionality to functions and methods, such as logging, memoization, and access control.
"""
#normal function
# def hello():
#     print("hello world")
# def add(a=5,b=6):
#     print(a+b)
# hello()
# add()

#decorative function
# def greet(fx):
#     print("good morning")
#     fx()
#     print("thanks for using function")
#     return fx

# @greet
# def hello():
#     print("hello world")
# hello()


#example:
# import logging

# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated

# @log_function_call
# def my_function(a, b):
#     return a + b
# my_function(5,6)


#harry's example
def greet(fx):
  def mfx(*args, **kwargs): # args and kwargs tab use karo jab argument malum nahi ho
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx # return karna jaruri hai nhi to warning aa jaygi

@greet
def hello():
  print("Hello world")

@greet
def display(*numbers): #n number of argument lega or use tuple bana lenga number namka or fir tuple k jese unhe use kar saktey ho
  for i in numbers:
    print(i)

# greet(hello)() #greet me hello function pass kara hai dono hi same hai
hello()
# greet(add)(1, 2)
display(1, 2,3,4,5,6,7,8,9)