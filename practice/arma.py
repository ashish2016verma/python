n = int(input("Enter number"))
s = n
l = len(str(n))
print(l)
sum = 0
while n!=0: 
    r = n%10
    sum+=(r**l)
    n=n//10 
if sum==s:  
        print("Number is palindrome")
else:   
        print("number is not palindrome")


print('hello')