"""
python provides several ways to manipulate files.
file should be open first in any mode and closed after operation to save memory
syntax
file_pointer= open("file_name",'mode of open')

mode:
read r : it is default mode if mode is not specified
write w
append a
create c
text t
binary b

"""

#open and read
# f= open('myownmodule.py','r')
# print(f) #another way to read content of a file that is read()
# text=f.read()
# print(text)
# print(f.read())
# f.close()

#write on file : if not exists , than it will create file
# f= open('temp.txt','w')
# f.write("hello guys")
# f.close()

#write on file : if not exists , than it will create file ,
# f= open('temp.txt','a')
# f.write(" hello guys")
# f.close()

#with keyword : file automatically closed by using with keyword
# with open("temp.txt",'a') as f_ptr:
#     f_ptr.write(" hey i am inside")
