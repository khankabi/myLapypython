"""
python doc string are the string literals that appear right after the defination of function, method, class or module
rules:
neccessary to write at the first line of a function block
enclosed by single quote
accessed by doc attribute
it is not comment
"""
def square(n):
    ''' takes in a number n. returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)



"""
PEP 8 - python enhancement proposal that provides guidelines and best practices on how to write python code.
"""

"""
# the Zen of python : it is an easter egg, very beautifull poem for programming to comparision
import this
# output:
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

"""
