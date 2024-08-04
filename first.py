
'''print("hello")  
a=int(input())  
print(a)    
if(a>10) :  
    print("your age is",a)
else:   
    print("your age not match ") 
      

print("......................") 
b=input("enter a string")   
for i in b:     
    print(i)

print("................")    
for i in range(1,10):   
    print(f"{a} x {i}={a*i}") '''

# Get user input as a comma-separated string
user_input = input("Enter the elements of the array, separated by commas: ")

# Convert the input string to a list of integers
array = [int(x.strip()) for x in user_input.split(',')]

# Reverse the array using slicing
reversed_array = array[::-1]

# Print the reversed array
print("Reversed array:", reversed_array)
