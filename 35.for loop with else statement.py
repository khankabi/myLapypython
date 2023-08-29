"""
python allows us to use else clause with for loop or while loop
"""
for i in range(5):
    print(i)
else:
    print("done")



#special condition - loop khatam huva hai after break statement means it also ignore else clause
print("\n\n\n")
for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("done")