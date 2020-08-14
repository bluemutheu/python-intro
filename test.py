unique = set ([2,3,5,5,6,6,6])

print (unique)

n = int (input())
if (n%2 > 0) or ((n%2 == 0) and (n>=6 and n <=20)):
    print ("weird")
elif ((n%2 == 0) and (n >=2)and (n<= 5)) or ((n%2 == 0) and (n>20)):
    print ("Not weird")
else : print ('This is the end')