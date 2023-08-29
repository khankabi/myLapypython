"""
match case is a new feature in python ( switch statement)
x is the variable to match
note that there is no need to write break statement like c/c++, means only one case will match other will be ignored by compiler
last case is default case
if you want to compare something like case 2 3 4. you need 'case _ if (condition)'
"""
x=int(input("Enter a number 0 to 100:"))
match x :
    case 0:
        print('this is zero')
    case _ if x>=1 and x<=50:
        print("the number is :",x,"between 1 to 50")
    case _ if (x>=50 and x<=100):
        print("the number is :",x,"between 50 to 100")
    case _ if x>=101:
        print("the number is :",x,"morethan 100")
    case _:
        print("wrong input")
