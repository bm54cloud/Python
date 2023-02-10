import random

numbers = list(range(0,5))

print(numbers)

# Use a for loop when it is a fixed number of times
for number in numbers:
    print(number)
    

for i in range(5):
    print("Hi")

# Use while loops when you do not have a fixed number of times

number = random.randint(0,10000)
counter = 0 # counter variable is common with while loop because you want to know how many times it ran
while number != 55:
    if (counter != 10000): # this will try to get the number within 10000 tries
        number = random.randint(9,10000)
        counter = counter + 1
    else:
        break # if number not met in 10000 tries, then it will break
print(counter, number)

# for -> while (do not do this)
number = random.randint(0,10000)
for i in range(10000):
    if(number != 55):
        number = random.randint(0,10000)
    else:
        break
print(i, number)

# while -> for
number = random.randint(0,5)
counter = 0
while(counter< len(numbers)):
    print(numbers[counter])
    counter = counter + 1
    