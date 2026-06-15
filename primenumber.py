start =int(input("eneter first number"))
end = int(input("enter end number"))
for i in range(start,end+1):    
    flag=0
    for j in range(2,i): 
        if i%j==0:  
            flag=1
            break
    if flag==0: 
        print(i,end=" ")     
