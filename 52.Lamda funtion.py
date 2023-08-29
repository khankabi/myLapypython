"""
in python, it is a small anonymous function without name. it is defined using the lambada keyword
syntax:
function_name=lambda arguments:expression


also lambda function can be used without name
refer example 3
"""
#normal method
# def double (x):
#     return x*2

#lambda method - one line function in python
double= lambda x:x*2
cube=lambda  x : x*x*x
avg = lambda x,y=10 : (x+y)/2
print(double(5))
print(cube(5))
print(avg(5))


#complex
def appl(fx,value):
    return 6 + fx(value)
print(appl(cube,2))


#ex2
# used to pass function as argument, also refer previous example
#function that takes function as argument known as higher order funtion

print(appl(lambda x:x*x,3))
