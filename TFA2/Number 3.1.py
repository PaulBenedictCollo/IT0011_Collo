first_name = input("Please Enter First Name: ")
last_name = input("Please Enter Last Name: ")
age = input("Please Enter Age: ")

full_name = first_name + " " + last_name
print("Full Name: ", full_name)

sliced_name = first_name
x = slice(3)
print("Sliced Name: ", (sliced_name[x]))

greeting = "Hi there {fname}, You are {yrs} years old!" .format(fname = sliced_name[x], yrs = age)
print(greeting)