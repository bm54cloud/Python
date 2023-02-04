# Allow user to input how many EC2 instances they want names for and output the same amount of unique names.
# Allow user to input the name of their department that is used in the unique name.
# Generate random characters and numbers that will be included in the unique name.
# Only Marketing, Accounting, and FinOps departments should use this generator. 
# List these departments as options 
# If a user puts another department, print a message that they should not use this Name Generator. 
# Be sure to account for incorrect upper or lowercase letters in the correct department. 

import random, string 

instancenum = input("How many instances do you want to create names for? ")
department = input("What is the name of your department (Marketing, Accounting, FinOps)? ")

if department.lower() == 'marketing':
    print("Here are your unique EC2 instance names: ")
    for i in range(int(instancenum)):
        x = (department.capitalize() + ''.join(random.choices(string.ascii_letters + string.digits, k=16)))
        print(x)
elif department.lower() == 'accounting':
    print("Here are your unique EC2 instance names: ")
    for i in range(int(instancenum)):
        x = (department.capitalize() + ''.join(random.choices(string.ascii_letters + string.digits, k=16)))
        print(x)
elif department.lower() == 'finops':
    print("Here are your unique EC2 instance names: ")
    for i in range(int(instancenum)):
        x = ('FinOps' + ''.join(random.choices(string.ascii_letters + string.digits, k=16)))
        print(x)
else:
    print("Your department is not authorized to use this Name Generator")




