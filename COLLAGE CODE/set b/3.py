""" Write a python script which accept an integer value as command line and print "ok" if value is
between 1 to 50 (both inclusive) otherwise it prints "out of range"."""

number =int(input("Enter a Number : "))
if(number >0 and number<51):
    print("OK")
else:
    print("out of range")
