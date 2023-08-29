"""
Single Inheritance in Python
Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. This is the simplest and most common form of inheritance.

Syntax
The syntax for single inheritance in Python is straightforward and easy to understand. To create a new class that inherits from a parent class, simply specify the parent class in the class definition, inside the parentheses, like this:

class ChildClass(ParentClass):
    # class body

"""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()




"""
# If we want to create a new class for a specific type of animal, such as a dog, we can create a new class named "Dog" that inherits from the Animal class.


The Dog class inherits all the attributes and behaviors of the Animal class, including the __init__ method and the make_sound method. Additionally, the Dog class has its own __init__ method that adds a new attribute for the breed of the dog, and it also overrides the make_sound method to specify the sound that a dog makes.

Single inheritance is a powerful tool in Python that allows you to create new classes based on existing classes. It allows you to reuse code, extend it to fit your needs, and make it easier to manage complex systems. Understanding single inheritance is an important step in becoming proficient in object-oriented programming in Python.
"""


class emp:
    count=0
    def __init__(self,name):
        # print(emp.count)
        self.name=name
        emp.count+=1
        self.id=emp.count
    def __str__(self):
        return f"{self.name} : {self.id}"
class dept(emp):
    def __init__(self,name,lang):
        self.lang=lang
        super().__init__(name)
    def __str__(self):
        return f"{self.name} : {self.id} dept: {self.lang}"

ob=emp("sonu")
print(ob)
ob2=dept("samir","python")
print(ob2)
ob2=dept("afzal","c++")
print(ob2)
ob2=dept("aman","web tech")
print(ob2)