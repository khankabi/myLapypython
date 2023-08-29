"""
Python Class and Objects
A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.

Creating a Class:
Let us now create a class using the class keyword.


"""
class Details:
    name = "Rohan"
    age = 20

"""
Creating an Object:
Object is the instance of the class used to access the properties of the class Now lets create an object of the class.
"""

# Example:
obj1 = Details()


# Now we can print values:

# Example:
class Details:
    name = "Sonu"
    age = 20
obj1 = Details()
print(obj1.name)
print(obj1.age)


# Output:
# Rohan
# 20


#example
class person:
    name="samir"
    age=18
    gender="male"
obj=person()
print(f"my name is {obj.name}.\ni am {obj.age} old.\ni am {obj.gender}")



#complex examples:
# harry's example
class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(this): #def into(self): #bas ek identifies chahiye jo this keyword ki act kare
    print(f"{this.name} is a {this.occupation}")

"""
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It must be provided as the extra parameter inside the method definition.

#actual example me self identifier use kiya hai lekin ham koi bhi name le sakatey hai

 self automatically pass hota hai jab bhi constructor ya self parameter pass hoti hai
mtlb k self ko bhi argument gino lekin pass automatic hoga jab object ko liye method call karoge
"""


a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()


#mine example
class emp:
   name="sonu"  #this is class variable , there are two types of variable in class , watch 66 tutorial
   age=80
   dept="hr"
   def display(self):
      print(f"emp name is {self.name} of {self.dept}. he is {self.age} old")
a=emp()
b=emp()
c=emp()


a.name="aman"
a.age=70
a.dept="money"

b.name="afzal"
b.age=60
b.dept="relationship"
print(emp.name)

a.display()
b.display()
c.display()