#Lists
#ways of creating lists
empty = []
e2 = list()
print (type(empty))

#ensuring that casesenitivity is 'removed'
towns = ['Nakuru'.casefold(), 'Lodwar'.casefold(), 'Mombasa'.casefold(), 'Kiambu'.casefold(), 'Lodwar'.casefold(),'Lodwar'.casefold()]
towns2 = ['Thika', 'Kisumu']
task ='nakuru' in towns
print (task)

allTowns = towns + towns2
print (allTowns)
print (towns [0:4])

repTowns = towns2 * 2
print (repTowns)
 
# Tuples
myTuple = ("mouse", [8, 4, 6], (1, 2, 3))


print (myTuple [1][2])
 

#Dictionaries
months = {'1' : 'January','2' : 'February','3' : 'March', '4' : 'April', 5 : 'May', 5.0 : 'July', '5' : 'June' }
print(months[5])
print(months[5.0]) #restored since 5 and 5.0 are the same
print(months['5'])

#set
numbers = [1,2,3,4,5,6,7,7,8,8,2,1,3]

mySet = set(numbers)
print (mySet)

#_____________Question One_______________________
#a
taskList = [23, 'Jane', ['Lesson 23', 560, {'currency' : 'KES'}], 987, (76,'John')]
print (taskList)
print (type(taskList[0]))
print (type(taskList[1]))
print (type(taskList[2]))
print (type(taskList[3]))
print (type(taskList[4]))

#b
print (taskList [2][2]['currency'])

#c
print(taskList [2][1])

#d
print (len(taskList))

#e
taskList[3] = 789
print(taskList)

#f
#Tuples are immutable you can not change its values
taskList[-1] =  (76, "Jane")
print(taskList)
#_____________________Question 2_________________
# import math
ls1 = [123,34,54645,34,5]
print (ls1 )
# print(math.ceil(123,34,54645,34,5))
print (ls1.sort())
print (ls1)
print (ls1[-1])

#____________________Question 3____________________
profit= {'cost_price': 32.67, 'sell_price': 45.00,  'inventory': 1200 }
print (profit)
shelf_price = (profit['cost_price'] * profit ['inventory'])
print (shelf_price)
selling_price = (profit['sell_price'] * profit ['inventory'])
print (selling_price)
profit_sell = selling_price - shelf_price
print (profit_sell)

#_______________________Question3___________________________
n = int (input())
i = 0
while (i<n):
    print(i**2)
    i+=1

#______________________Question1_______________________________

n = 5
scores = [10,10,10,5,4]
mx = max(scores [0],  scores [1])  

secondmax = min(scores [0], scores [1])  

for i in range(2,n):  
    if scores [i] > mx:  
        secondmax = mx 
        mx =  scores [i]  
    elif scores [i]> secondmax and mx != scores [i]:  
        secondmax=  scores [i] 
    else: 
        if secondmax == mx: 
            secondmax = scores [i] 
  
print("Second highest number is : ",str(secondmax)) 

#_____________________Question2_______________________________

n = int (input())

if n %2 == 0 and n >= 2 and n <= 5:
    print ('nt weird')
elif n %2 == 0 and n >= 6 and n <= 20:
    print('Weird')
elif n %2 == 0 and n > 20 :
    print('not weird')
else:
    print('weird')

unique = set ([2,3,5,5,6,6,6])

print (unique)




