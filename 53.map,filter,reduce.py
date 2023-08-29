"""they are used with any data type such as list, string, tuple etc"""


#MAP:argument(operation or/on value)
def cube(x):
    return x*x*x
print(cube(2))


#normal approach : list , make empty list, perform operation
l=[1,2,4,6,4,3]
newl=[]
for item in l:
    newl.append(cube(item))
newl = print(newl)

#map approach : map() used to access each item in object, two argument required 1. operation 2. on whom
#1 tp
maped=map(cube,l)
maped = list(maped)
#2 tp
#operation or kispe , do argument hoti hai map() ki
maped2= map(lambda x: x*x,l)
maped2=list(maped2)
print(maped2)
print(maped)

#FILTER : argument(filter condition or value) - vo value return karega jo condition ko pass kar degi jise filtering boltey
def filter_function(a):
    return a>4 # will return true or false
fltr= list(filter(filter_function,l))
print(fltr)


#REDUCE : why i am getting error
# def mysum(x,y):
#     return x+y
# numbers=[1,2,3,4,5,6,7,8,9,10]
# sum = reduce(mysum,numbers)
# print(sum)
