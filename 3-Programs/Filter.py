number = [0,1,2,3,4,5,6,7,8,9]

y = list(filter(lambda x:x%2==0, number))
print(y)

y = list(filter(lambda x:x%2!=0, number))
print(y)