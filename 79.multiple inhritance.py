"""
Multiple Inheritance in Python
Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.

Syntax
In Python, multiple inheritance is implemented by specifying multiple parent classes in the class definition, separated by commas.

class ChildClass(ParentClass1, ParentClass2, ParentClass3):
    # class body


In this example, the ChildClass inherits attributes and methods from all three parent classes: ParentClass1, ParentClass2, and ParentClass3.

It's important to note that, in case of multiple inheritance, Python follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different parent classes. The MRO determines the order in which parent classes are searched for attributes and methods.


Method Resolution Order :
Method Resolution Order(MRO) it denotes the way a programming language resolves a method or attribute. Python supports classes inheriting from other classes. The class being inherited is called the Parent or Superclass, while the class that inherits is called the Child or Subclass. In python, method resolution order defines the order in which the base classes are searched when executing a method. First, the method or attribute is searched within a class and then it follows the order we specified while inheriting. This order is also called Linearization of a class and set of rules are called MRO(Method Resolution Order). While inheriting from another class, the interpreter needs a way to resolve the methods that are being called via an instance. Thus we need the method resolution order.

"""

'''example:'''
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color

class Dog(Mammal,Animal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed

    def make_sound(self):
        print("Bark!")


obj=Dog("rocky","german","brown")
obj.make_sound()
print(Dog.mro()) #order of search

'''
          .-'-.
        /'     `\
      /' _.-.-._ `\
     |  (|)   (|)  |
     |   \__"__/   |
     \    |v.v|    /
      \   | | |   /
       `\ |=^-| /'
         `|=-=|'
          | - |
          |=  |
          |-=-|
    _.-=-=|= -|=-=-._
   (      |___|      )
  ( `-=-=-=-=-=-=-=-` )
  (`-=-=-=-=-=-=-=-=-`)
  (`-=-=-=-=-=-=-=-=-`)
   (`-=-=-=-=-=-=-=-`)
    (`-=-=-=-=-=-=-`)
jgs  `-=-=-=-=-=-=-`
'''
