import random

# Create an empty list
var = []

print(type(var))

# Lists can contain different data types
var2 = [151, 251, 386, "009"]
print(var2)

var2.append(493) # inplace functions don't require storing in a variable
print(var2)

# dir will give you all the hidden variables and functions you can call from this variable type
# print(dir(var2)) 

numbers = [0, 1, 2, 3, 4]
print(numbers)

# Iterate through a list
for number in numbers:
    print(number * 2)

number_list = list(range(2,10))
print(number_list)

print(number_list[3]) # indexing starts at 0, output should be 5

print(len(number_list))

list_of_list = [[random.randint(0,10) for i in range(5)] for j in range(5)]
print(list_of_list)
print(list_of_list[2][3])

for l in list_of_list:
    print(l)
    
print(list_of_list[2][3])