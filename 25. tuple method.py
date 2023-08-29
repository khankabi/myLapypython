#operation on tuple create new tuple but not affect actual tuple





"""
operations can change actual list item but you cannot change tuple items directly so you need to
1. typecast it into list
2. perform operations
3. again typecast it into tuple
4. your tuple is changed
"""



print("\n\n\n")
names= ("spain","italy","india","england","germany")
print("original:         ",names)
temp=list(names) #tuple conversion to list
temp.append("pakistan")  # add item
temp.pop()  # remove last item
temp[2]="bharat"  # change item
# names=tuple(temp) # again conversion of list into tuple
print("after operations: ",temp)
print("after operations: ",names)



#we can concatenate two tuple directly
print("\n\n\n")
state=("gujrat","maharastra")
new= state+names
print("new tuple is : ",new)



#couting occurance of item in tuple
cnt= names.count("italy")
print(cnt)


#try to change tuple : it will lead to attribute error
names.append("nashik")
print(names)