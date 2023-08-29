"""
there are four types of arguments and return statement
1. Default argument
2. keyword argument
3. required argument
4. variable-length argument
"""
#Default argument: we can set values of argument , if user not submit the value this value consider as value of argument
def average(a=1,b=5):
    print("The average is : ",(a+b)/2)
average()
average(2)

#keyword argument: order of argument does not metter , you can pass argument separtly means , way of callling argument:-
average(b=45,a=10)


#required argument: argument which is not set by defualt is neccessary to provides by user- kisi or ka do ya na do required argument dene hi padege
def average2 (a,b=5):
     print("The average 2  is : ",(a+b)/2)
average2(a=12)


#variable -length argument- here the number of argument is in variable size by using * symbol
def average3(*numbers):
     sum=0
     for i in numbers:
          sum+=i
     print("the average 3  is : ",sum/len(numbers))
average3(4,5,6,7)