"""
enumerate function is a built in function in python that allows you to loop over a sequence and get the video and value of each element in the sequence at the same time. here's a basic example of how it works.

The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:

The enumerate function is often used when you need to loop over a sequence and perform some action with both the index and value of each element. For example, you might use it to loop over a list of strings and print the index and value of each string in a formatted way:


linter is red line that represents an error
"""


marks = [12, 56, 32, 98, 12,  45, 1, 4]
index = 0
for mark in marks:
  print(mark)
  if(index == 3):
    print("Harry, awesome!")
  index +=1


#enumerate function for above code
for index, mark in enumerate(marks, start=1):
  print(mark)
  if(index == 3):
    print("Harry, awesome!")

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)


# Loop over a list and print the index (starting at 1) and value of each element
# fruits = ['apple', 'banana', 'mango']
# for index, fruit in enumerate(fruits, start=1):
#     print(index, fruit)


tup = ("samir","yasin","shaikh")
for index,i in enumerate(tup , start=1):
  print(index,i)
  if(index==2):
    print("he is my father")