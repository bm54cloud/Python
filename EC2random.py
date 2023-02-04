# Allow user to input how many EC2 instances they want names for and output the same amount of unique names.
# Allow user to input the name of their department that is used in the unique name.
# Generate random characters and numbers that will be included in the unique name.
# Only Marketing, Accounting, and FinOps departments should use this generator. 
# List these departments as options 
# If a user puts another department, print a message that they should not use this Name Generator. 
# Be sure to account for incorrect upper or lowercase letters in the correct department. 

instancenum = input("How many instances do you want to create names for? ")
department = input("What is the name of your department (Marketing, Accounting, FinOps)? ")

if department.lower() == 'marketing':
    print("Here are your unique EC2 instance names: ")
    import random
    for i in range(int(instancenum)):
        print(department.capitalize(), random.randrange (9999999), sep="")
elif department.lower() == 'accounting':
    print("Here are your unique EC2 instance names: ")
    import random
    for i in range(int(instancenum)):
        print(department.capitalize(), random.randrange (9999999), sep="")
elif department.lower() == 'finops':
    print("Here are your unique EC2 instance names: ")
    import random
    for i in range(int(instancenum)):
        print('FinOps', random.randrange (9999999), sep="")
else:
    print("Your department is not authorized to use this Name Generator")




