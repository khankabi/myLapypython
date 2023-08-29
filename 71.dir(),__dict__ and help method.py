"""
dir(), __dict__ and help() methods in python
We must look into dir(), __dict__() and help() attribute/methods in python. They make it easy for us to understand how classes resolve various functions and executes code. In Python, there are three built-in functions that are commonly used to get information about objects: dir(), dict, and help(). Let's take a look at each of them:

The dir() method
dir(): The dir() function returns a list of all the attributes and methods (including under methods) available for an object. It is a useful tool for discovering what you can do with an object. -- returns all function for that particular variable or other entity

The __dict__ attribute
__dict__: The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.


The help() mehthod
help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods.


In conclusion, dir(), dict, and help() are useful built-in functions in Python that can be used to get information about objects. They are valuable tools for introspection and discovery."""


# dir
# x = [1, 2, 3]
# print(x.__dir__()) # print(dir(x))


#sabkuch batayega
# x=1
# print(x.__dir__()) # print(dir(x))
# print(x.__neg__()) # print(dir(x))


#dict - class k sare attribute as a dictionary bana k show karega
class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
      self.version = 1


p = Person("John", 30)
print(p.__dict__)

#help()
print(help(Person))
