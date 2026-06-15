'''n  = [4,6,3,4]
l  = len(n)
sum = 0
for i in n: 
    sum+=i
print(sum)'''
#user input in array in multiple line
'''n = int(input())
arr=[]
for i in range(0,n):  
    element = int(input()).strip().split()[:n]
    arr.append(element)
print(arr)'''
# user input in one line
n = int(input())
arr = [int(x) for x in n.split()]
print(arr)