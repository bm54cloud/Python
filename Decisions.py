import random
# Print a random number from 0 through 10
# BASIC
number = random.randint(0,10)

if(number < 6):
    print("small number")
elif(number > 6):
    print("big number")
else:
    print("number is 6")
    
print(number)

# To see all the modules available for random
# print(dir(random))

# %%

# ADVANCED
number = random.randint(0,10)
thresh = 4

if(number < thresh): # 0, 1, 2, 3, 4, 5, 6, 7
    print("small number")
elif(number > thresh): # 8, 9, 10
    print("big number")
else: # This is not doing anything bc 6 is included in the first statement
    print("number is ", thresh)
    
print(number)