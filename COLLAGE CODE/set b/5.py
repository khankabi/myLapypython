"""Write a python script to accept two numbers as range and display multiplication table of all numbers
within that range"""
def multiplicationTable(n):
   
    for i in range(1,11):
        print(f" {n} X {i} = {i*n}",end="\n")
    

number= int(input("Enter a Number : "))
for i in range(1,number+1):
    print("\n Multiplication table of ",i)
    multiplicationTable(i)
        
