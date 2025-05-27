# Method 1 (fixed number)

result = 1
for i in range(1,5):
    result = result * i
print(result)


# Method 2 (Given number)

result = 1
num = 7
for i in range(1,num+1):
    result = result * i
print(result)


# Method 3  (User input)

result = 1
num = int(input("Enter a number : "))
for i in range(1,num+1):
    result = result * i
print(result)


# Method 4 (Using recursions)

def fact(num):
    if num ==0:
        return 1
    
    else:
        return num * fact(num-1)

n = int(input("Enter a number : ")) 
print(fact(n))