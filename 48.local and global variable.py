""" agar local me same name variable nahi hai to global ko access karega nahi to local wale ko karega
refer example 2

global keyword
global variable can also access through global keyword , used to manipulate global variable in local space
"""

# with local variable
x = 4
print("outside : ", x)


def hello():
    x = 5
    print("inside : ", x)
    print("hello sonu")


hello()
print(f"{x} is global variable")
x = 786
print(f"{x} is global variable")


# without local variable  example 2
print("\n\n\n")
x = 4
print("outside : ", x)


def hello():
    print("inside : ", x)
    print("hello sonu")


hello()
print(f"{x} is global variable")
x = 786
print(f"{x} is global variable")


print("\n\n\n")
x = 4
print("outside : ", x)


def hello():
    global x
    # x=5
    print("inside : ", x)
    print("hello sonu")


hello()
print(f"{x} is global variable")
x = 786
print(f"{x} is global variable")
