"""Write a program to accept a binary number and convert it inoro decimal number"""

def binToDec(n):
    decimal = int(n,2)
    print(f"The Decimal Value Is {decimal}")
    
#body
bin_string = input("Enter a Binary Number : ")
binToDec(bin_string)
