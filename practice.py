'''a=int(input("enter a number"))  
if a>0: 
    print("Number is postive")
else:   
    print("Number is negative")'''
#2
'''a=int(input("enter a number"))
if a%2==0:  
    print("number is even")
else:   
    print("number is odd")'''
#3
'''a=int(input("enter a number"))
sum = 0
for i in range(0,a):    
    sum+=i
print(sum)'''
#4
'''a=int(input("enter a number"))
for i in range(2,a):  
    if a%i==0:  
        print("numebr is not prime")
        break
    else:
        print("numbr is prime")    
        break'''
num = 3
flag = 1
for i in range(2,num):
  if num%i==0:
    flag = 0
    break
if flag == 0:
  print('Not Prime')
else:
  print(" Prime")
