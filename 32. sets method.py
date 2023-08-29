"""

"""
s1={1,2,5,6}
s2={3,6,7}
print(s1,s2)

# union/combination of two sets
# print("\n\n\n")
# print(s1.union(s2))


#updation of set using update() function
# print("\n\n\n")
#combine s2 into s1 - this will affect original set
# print("\n\n\n")
# s1.update(s2)
# print(s1)
# print(s2)


#common finding method
# print("\n\n\n")
# print("common in both sets")
# s1.intersection_update(s2)
# print(s1)
# print(s1.intersection(s2)) #not affect actual set only update keyword can update actual sets
# print(s1)


#difference finding method
# print("\n\n\n")
# print(s1.difference(s2)) # dono me kya difference hai
# print(s1.symmetric_difference(s2)) # vo sari values jo common nahi hai
# s1.symmetric_difference_update(s2) #to update actual set
# print(s1)


#disjoint - dono me similarities hai ya nahin , false = hai true = nahin hai
# print(s1.isdisjoint(s2))


#superset and subset = s1 holding all values of s2 or not is yes s1 is superset and s2 is subset of s1
# print(s1.issuperset(s2))
# print(s1.issubset(s2))

#to remove item from set without error
# s1.remove(2)
# print(s1)


#to remove item from set with error
# s1.discard(2)
# print(s1)


#to remove random item from set with display what is removed
# item=s1.pop()
# print(s1)
# print(item)

#to delete entire set
# del s1
# print(s1)

#checking using if
a=int(input("Enter number between 1 to 10 : "))
if a in s1:
    print("yes, it is exists")
else:
    print("not exists")