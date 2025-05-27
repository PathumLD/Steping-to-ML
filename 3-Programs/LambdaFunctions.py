# Normal

def area(a):
    return a*a

print(area(5))

# Lambda

area = lambda x : x*x
print(area(4))

area = lambda x,y : x*y
print(area(4,5))


def price():
    return lambda no_of_apples, unit_price : no_of_apples * unit_price

print(price()(25, 30))  
