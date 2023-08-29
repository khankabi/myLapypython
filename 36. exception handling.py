"""
the process of responding to unwanted or unexpected events when a computer program runs. exception handling deals with these events to avoid the program or system crashing and without the process exception would disrupt the normal operation of a program.


try block me vulnerable code line likho jisme error aa sakti hai
then try block error raise karega jo
except block me jayga or exception handle honga
try k bad except block hona jaruri hai

syntax:
try:
    some code
except:  or except Exception as identifier :
"""


a=input("Enter the number: ")
print(f"multiplication table of {a} is : " )


#first example
# try:
#     for i in range(1,11) :
#         print(f"{int(a)} X {i} = {int(a)*(i)}")
# except Exception as e_message:
#     print(f"sorry, some error has occured , {e_message}")
#except:
    # print("sorry, some error has occured ")


#second example
try:
    num=int(input("Enter an integer"))
    a=[6,3]
    print(a[num])
except ValueError:  #built in error handler in python
    print("Number entered is not an integer")
except IndexError:
    print("index error")
except:
    print("sorry for incovinience !!!")


print("thank you")