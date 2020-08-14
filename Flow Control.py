# If the number is positive, we print an appropriate message
#__________________________Conditional Operators_____________________________________


num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = 5
if num > 0:
    print("This will execute")
    print("This will execute")


num = -1
if num > 0:
    print(num, "is a positive number.")

num = 3
print (num)
res = num > 0 or num%2 == 0
print (res)

num = 3
print (num)
res = num > 0 and num%2 == 0
print (res)

#print marks

grade = 20

if grade >= 70:
    print('A')
elif grade <70 and grade >= 60:
    print('B')
elif grade <60 and grade >= 50:
    print ('C')  
elif grade <50 and grade >= 40:
    print ('D')  
else:
    print('E')
if grade > 50:
    print('Pass')
else:
    print ('Fail') 

#Nested if
'''In this program, we input a number
check if the number is positive or
negative or zero and display
an appropriate message
This time we use nested if statement'''

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
    
grade = 45  
    
if grade >= 70:
    print('A')
else:

    if grade >= 60:
        print('B')
    else:
        if grade >= 50:
            print('C')
        else:
            if grade >= 40:
                print ('D')
            else:
                print('E')



