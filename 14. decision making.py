a= int(input("Enter your age:"))
print("your age is :",a)


"""
INDENTATION
Python indentation is a way of telling a Python interpreter that the group of statements belongs to a particular block of code. A block is a combination of all these statements. Block can be regarded as the grouping of statements for a specific purpose.
JUST GIVE SPACE AFTER STATEMENT TO REFER AS A BLOCK
"""
#and , or , xor k symbol illegal hai python me
if(a>18 and a<=60):
    print("you can drive!!!")
    print("drive safly please!!!")
elif(a==18 or a<=10):
    print("you can apply for licence")
    print("learn how to drive!!!")
elif(a>=60 ):
    print("ghar per aaram kro please")
elif(not a >0):
    print("negative  number")
else:
    print("you cannot drive!!!")