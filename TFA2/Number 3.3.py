first_name = first_name = input("Please Enter First Name: ")
last_name = input("Please Enter Last Name: ")
age = input("Please Enter Age: ")
contact_number = input("Please Enter Contact Number: ")
course = input("Please Enter Course: ")

student_info = "First Name: {fname} \n Last Name: {lname} \n Age: {yrs} \n Contact Number: {number} \n Course: {degree}" .format(fname = first_name, lname = last_name, yrs = age, number = contact_number, degree = course)
with open("students.txt", "a") as file:
        file.write(student_info)
        
print("Student Information has been saved successfully.")
