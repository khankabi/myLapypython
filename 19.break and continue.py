#to stop iteration
for i in range(12):
    if(i == 10):
        print("thank you")
        break
    print("5 X",i+1,"=", 5*(i+1))


#to skip something
print("\n\n\n")
for i in range(12):
    if(i == 10):
        print("thank you")
        continue
    print("5 X",i+1,"=", 5*(i+1))



#how to implement do while loop in python
#pehele loop ko infinite kardo or fir do block likho then if statement likho jo while ki tarah perform karega
while True:
    num=int(input("Enter a positive number:"))
    print(num)
    if not num>0:
        break
