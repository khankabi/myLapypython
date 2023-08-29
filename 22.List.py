""" readme
list is very imporant in python
used to store multiple item under single name
enclosed by square bracket
also you can store different datatype item
accessed by square bracket notation just like array
"""
marks=[3,"b","sonu",5.5,True]
print(marks)

#type of marks using type() function
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])



#negative indexing - just thing as minus number of element by negative index, example is below
print("\n\n\n")
print(marks[-3])
print(marks[len(marks)-3])
print(marks[2-3])



#how check for element exists in list or not
print("\n\n\n")
if "sonu" in marks:
    print("YES")
else:
    print("NO")
#Note:datatype of searching element matters in list


#range access
print("\n\n\n")
print(marks)
print(marks[1:])#blank refer as end value
print(marks[1:3])
print(marks[0:5:2]) #last is step during iteration



#list comprehension
"""
 - used for creating new lists from other iterables like lists, tuples,sets and even in array and string
 - syntax: list_name=[item_name for item in iterable if condition]
 """
print("\n\n\n")
lst=[i for i in range(10) if i%2==0] # only take numbers that divisiable by 2
lst2=[i for i in range(10)] #( without condition is also ok) it will take all numbers as a list items
print(lst)
print(lst2)
