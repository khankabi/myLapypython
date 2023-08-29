#tuple is similer to list but you cannot change the values of tuple  , means it is immutable, it is use rounded brackets
tup=(1,5,2,6,78,61.7,4,32,12.5,65,"sonu",64,92,84,"shaikh",103)
print(tup)
print(type(tup))
print("items in tuple is : ",len(tup))
print(tup[0])
print(tup[1])
print(tup[-2])
print(tup[3])

# for i in tup:
#     print(i)

if "sonu" in tup:
    print("yes sonu is exists in tuple")


#methods are similer in both list and tuple