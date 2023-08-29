#simple key and value pair , according to version it is ordered or not
dic={
    "harry":"human being",
    "spoon":"object"
}
print(dic)
print(type(dic))



print("\n\n\n")
dis={
    344:"harry",
    56:"sonu",
    45:"aman",
    567:"afzal",
    44:"adnan"
}
print(dis)
print(type(dis))


#accessing item
# print(dic["harry"])
# print(dis[44])


#for accessing multiple values
# for key in dis.keys():
#     print(f"the value corresponding to the key {key} is {dis[key]}")



# another method using items() function
# print(dis.items())



#another method using items() function with loop
# for key,value in dis.items():
#     print(f"the value of {key} is {value}")