# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

print("The sum is", sum)

num = list (range(1,101))
num7 = []
num5 = []
num6 = []
for i in num:
    if i%7 == 0:
        num7.append(i)
        
    if i%3 == 0 :
        num5.append(i)
        
    if i%5 == 0 :
        num6.append(i)
        
print (num7)
print (num5)
print (num6)
