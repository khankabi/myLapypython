"""
Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.

static method is created for class package, means if you want to combine a function with class without object. you can call static function by object name or class name also.

self method never takes self as a argument like other method in class


```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

result = Math.add(1, 2)
print(result) # Output: 3
```
In this example, the add method is a static method of the Math class. It takes two parameters a and b and returns their sum. The method can be called on the class itself, without the need to create an instance of the class.
"""

class Math:
  def __init__(self, num):
    self.num = num

  def addtonum(self, n):
    self.num = self.num +n

  @staticmethod
  def add(a, b):
      return a + b

# result = Math.add(1, 2)
# print(result) # Output: 3
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(Math.add(7, 2))
print(a.add(7, 2))


class emp:
   def __init__(self,n,n2):
      self.n=n
      self.n2=n2
      print("constructor is called")
   def show(self):
      print(f"{self.n} and {self.n2}")

   @staticmethod
   def state(n,n2):
      print(f"addition is {n+n2}")

ob=emp(5,6)
ob.show()
ob.state(ob.n,ob.n2)
emp.state(6,6)
emp.state(ob.n2,ob.n)
