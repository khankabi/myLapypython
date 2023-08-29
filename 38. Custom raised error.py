"""
we can raise error by using the raise keyword.
In python, we can raise custom errors by using the raise keyword.


Defining Custom Exceptions
In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

Here's the syntax to define custom exceptions:

class CustomError(Exception):
  # code ...
  pass
try:
  # code ...
except CustomError:
  # code...


This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc


error types in python
https://www.tutorialsteacher.com/python/error-types-in-python
"""

a = int(input("Enter any value between 5 and 9"))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")