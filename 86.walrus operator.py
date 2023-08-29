"""The Walrus Operator in Python
The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.

The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.
expression me rehte huve koi chize store karna hai to walrus operator ka use kartey
"""
# Here's an example of how you can use the Walrus Operator in a while loop:

numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())



# In this example, the length of the numbers list is assigned to the variable n using the Walrus Operator. The value of n is then used in the condition of the while loop, so that the loop will continue to execute until the numbers list is empty.

# names = ["John", "Jane", "Jim"]

# if (name := input("Enter a name:")) in names:
#     print(f"Hello, {name}!")
# else:
#     print("Name not found.")


#another example:
a=True
print(a:=False)

# #another example;
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
print(foods)

#without walrus
# foods =list()
# while True:
#     food=input("enter your favourite color : ")
#     if food=="quit":
#         break
#     foods.append(food)
# print(foods)

"""
It is important to note that the Walrus Operator should be used sparingly as it can make code less readable if overused.

In conclusion, the Walrus Operator is a useful tool for Python developers to have in their toolkit. It can help streamline code and reduce duplication, but it should be used with care to ensure code readability and maintainability.
"""