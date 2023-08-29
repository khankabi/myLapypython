"""
    Recursion: a situation when function calling itself multiple time until specifil condition satisfy
"""

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        print(n)
        return n * fact(n-1)
print(fact(4))