"""
readline() method used to read line from opened file : ex1
writline() method used to write line in opened file : ex2
"""

# ex1
# f=open("temp.txt","r")
# while True:
#     line=f.readline()
#     print(line)
#     if not line:
#         print(line,type(line))
#         break

# ex2
f = open("temp2.txt", "w")
lines = ["line1\n", "line2\n", "line3\n"]
f.writelines(lines)
f.close()
