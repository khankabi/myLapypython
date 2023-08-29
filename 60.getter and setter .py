"""

" kisi function ki return value ko ek property ki tarah use kar saktey hai"
Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator. Here is an example of a simple class with a getter method:

class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value


In this example, the MyClass class has a single property, _value, which is initialized in the init method. The value method is defined as a getter using the @property decorator, and is used to return the value of the _value property.
- matlb k ek function ko aesa bana do k vo property ban jaye

To use the getter, we can create an instance of the MyClass class, and then access the value property as if it were an attribute:

>>> obj = MyClass(10)
>>> obj.value
10


Setters
It is important to note that the getters do not take any parameters and we cannot set the value through getter method.For that we need setter method which can be added by decorating method with @property_name.setter

Here is an example of a class with both getter and setter:

class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        self._value = new_value


We can use setter method like this:

>>> obj = MyClass(10)
>>> obj.value = 20
>>> obj.value
20


In conclusion, getters are a convenient way to access the values of an object's properties, while keeping the internal representation of the property hidden. This can be useful for encapsulation and data validation.

function ki jagah direct function name se value access kar saktey
"""
# class MyClass:
#   def __init__(self, value):
#       self._value = value

#   def show(self):
#     print(f"Value is {self._value}")

#   @property  # getter
#   def ten_value(self):
#       return 10* self._value

#   @ten_value.setter
#   def ten_value(self, new_value):
#       self._value = new_value/10

# obj = MyClass(10)
# print(f"after : {obj._value}")
# # obj.ten_value = 67
# print(obj._value)
# print(obj.ten_value)
# obj.show()


class emp:
   def __init__(self,value):
    self.no=value
   def show(self):
    print(f"value is :  {self.no}")

    @property
    def getter(self):
      return self.no+100
    @getter.setter
    def getter(self,new_val):
       self.no=new_val/10


obj=emp(10)
obj.show()
obj.getter=obj.no
# obj.getter=67
print(obj.getter)
obj.show()
