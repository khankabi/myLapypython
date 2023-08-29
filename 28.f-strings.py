#f- string is used for string formatting - jaha jaha brackets hai waha ye variable ki values dal dega
letter = "hey my name is {1} and i am from {0}"
country="India"
name="Sonu"
print(letter.format(country,name))


#f-string - is used to placed a variable within string , above method is also used by it was not much effective
#thats why a new feature is introduced in python 3.6
# Syntax : f"string"
# without f, f string is not implemented
print(f"hey my name is {name} and i am from {country}")
#name ki jagah name ki value or country ki jagah country ki value aa jaygi

# example
price=49.5464
txt=f"todays price of chicken is {price:.2f}"
txt=f"todays price of chicken is {{price:.2f}}"
print(txt)