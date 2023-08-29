# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
# it was tough
def encode(str):
    if(len(str)<=3):
        # str1="".join(reversed(str))
        lst=list(str)
        lst.reverse()
        # print(lst)
        new_str="".join(lst)
        print(new_str)
        return (new_str)
    elif(len(str)>=3):
        lst=list(str)
        lst.reverse()
        lst.append(lst.pop(0))
        lst.insert(0,"cha")
        lst.append("str")
        new_str="".join(lst)
        print(new_str)
        return (new_str)
    else:
        print("nop")


str=input("Enter message for encoding : ")
new_str=encode(str)


def decode(str):
    if(len(str)<=3):
        # str1="".join(reversed(str))
        lst=list(str)
        lst.reverse()
        # print(lst)
        new_str="".join(lst)
        print(new_str)
        return (new_str)
    elif(len(str)>=3):
        lst=list(str)
        for i in range(0,3):
            lst.pop(0)
            lst.pop(-1)
        # print(lst)
        char=lst.pop(-1)
        lst=list(char)+lst
        lst.reverse()
        str="".join(lst)
        print(str)


    else:
        print("nop")
decode (new_str)
