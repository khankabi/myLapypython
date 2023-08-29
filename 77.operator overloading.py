"""Operator Overloading in Python: An Introduction
Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str.

Why do we need operator overloading?
Operator overloading allows you to create more readable and intuitive code. For instance, consider a custom class that represents a point in 2D space. You could define a method called 'add' to add two points together, but using the + operator makes the code more concise and readable:

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y) # prints 4, 6


How to overload an operator in Python?
You can overload an operator in Python by defining special methods in your class. These methods are identified by their names, which start and end with double underscores (__). Here are some of the most commonly overloaded operators and their corresponding special methods:

+ : __add__
- : __sub__
* : __mul__
/ : __truediv__
< : __lt__
> : __gt__
== : __eq__


For example, if you want to overload the + operator to add two instances of a custom class, you would define the add method:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


It's important to note that operator overloading is not limited to the built-in operators, you can overload any user-defined operator as well.

Conclusion
Operator overloading is a powerful feature in Python that allows you to create more readable and intuitive code. By redefining the behavior of mathematical and comparison operators for custom data types, you can write code that is both concise and expressive. However, it's important to use operator overloading wisely, as overloading the wrong operator or using it inappropriately can lead to confusing or unexpected behavior.
"""
# class Vector:
#   def __init__(self, i, j, k):
#     self.i = i
#     self.j = j
#     self.k = k

#   def __str__(self):
#     return f"{self.i}i + {self.j}j + {self.k}k"

#   def __add__(self, x):
#     return Vector(self.i + x.i,  self.j+x.j, self.k+x.k)
# v1 = Vector(3, 5, 6)
# print(v1)

# v2 = Vector(1, 2, 9)
# print(v2)

# print(v1 + v2)
# print(type(v1 + v2))



class emp:
  def __init__(self,n1,n2,n3):
    print("constructor is called")
    self.n1=n1
    self.n3=n3
    self.n2=n2
  def __str__(self):
    return f"{self.n1}n , {self.n2}n , {self.n3}n"
  def __sub__(self,x):
    return emp(self.n1-x.n1 , self.n2-x.n2 , self.n3-x.n3)
  def __add__(self,x):
    return emp(self.n1+x.n1 , self.n2+x.n2 , self.n3+x.n3)
#   ham aesa her operator k liye kar saktey

ob=emp(5,6,7)
print(ob)
ob2=emp(6,7,9)
print(ob2)
ob3=ob+ob2
print("sum of two object is : ",ob3)
ob4=ob-ob2
print("sub of two object is : ",ob4)
print("type after operation : ",type(ob3))


"""
note: us operator ko overload karne k liye in magic method ka use kartey or ham apne hisab se particular entity k liye inhe define kar saktey
link - https://docs.python.org/3/reference/datamodel.html
 Emulating numeric types¶
The following methods can be defined to emulate numeric objects. Methods corresponding to operations that are not supported by the particular kind of number implemented (e.g., bitwise operations for non-integral numbers) should be left undefined.

object.__add__(self, other)
object.__sub__(self, other)
object.__mul__(self, other)
object.__matmul__(self, other)
object.__truediv__(self, other)
object.__floordiv__(self, other)
object.__mod__(self, other)
object.__divmod__(self, other)
object.__pow__(self, other[, modulo])
object.__lshift__(self, other)
object.__rshift__(self, other)
object.__and__(self, other)
object.__xor__(self, other)
object.__or__(self, other)
These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |). For instance, to evaluate the expression x + y, where x is an instance of a class that has an __add__() method, type(x).__add__(x, y) is called. The __divmod__() method should be the equivalent to using __floordiv__() and __mod__(); it should not be related to __truediv__(). Note that __pow__() should be defined to accept an optional third argument if the ternary version of the built-in pow() function is to be supported."""