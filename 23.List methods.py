#there are vast range of method for list however some common are listed below
l=[1,2,3,4,5]
print("before : ",l)
# l.append(0) # to add item in list
# l.sort() # sort in ascending order
# l.sort(reverse=True) # reverse list order
# l.reverse() #reverse list order
# print(l.index(3)) # index of 3
# print(l.count(1)) #how many times 1 exists in list
# l.insert(1,899)# to add item at desired index , here at index 1 ,899 is added
# l.pop(3)#it will remove item at 3 index which is 4
print("after : ", l)



#special case
# m=l
# m[0]=0
# print(l)
#here m is a refernce to l , if you change in m list it directly reflect to l list , however in python it is not recommanded instead use copy()
# m=l.copy()
# m[0]=0
# print("list l",l)
# print("list m ",m)




#how to extend existing list
# m=[900,800,1000]
# l.extend(m)
# print(l)



#how to concatenate two list in one new list
# m=[900,100,200,122,456]
# l=[500,66,1665,6554,12,20]
# k=m+l
# print(k)
