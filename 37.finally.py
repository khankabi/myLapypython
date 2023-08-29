"""
it is also part of exceptiuon handiling. when we handle exception using the try and except block. we can include a finally block at the end.
it is always executed , so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with deighful message.
 syntax:
 try:
    statemnets which could generate
 except:
    solution of generated error
 finally:
    block of code which is going to execute in any situation

note: finally always execute hoga age function return hogya to bhi kuch bhi ho jaye leking finally execute hoga
normal statement ( without finally) function return hone k bad lines ignore ho jaygi lekin finally me execute karna hi honga agar vo
return huve to bhi
example:
"""


def func():
    try:
        l=[1,2,564,7]
        i=int(input("Enter the index:"))
        print((l[i]))
        return 1
    except:
        print("sone error occured")
        return 0
    finally:
        print("i am always executed")

x=func()
print(x)