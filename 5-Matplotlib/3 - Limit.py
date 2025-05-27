import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [2,4,6,8])

left, right = plt.xlim(0, 5)  
    #   left, right = plt.xlim(1) -> only left will change
    #   left, right = plt.xlim(right= 8) -> only right will change
    #   left, right = plt.xlim(left=0, right=5)

bottom, top = plt.ylim(0,10)
    #   top, bottom = plt.ylim(10) -> only bottom will change
    #   top, bottom = plt.ylim(top=20) -> Only top will change
    #   top, bottom = plt.ylim(bottom=0,top=10)

print(left)
print(right)
print(bottom)
print(top)

plt.show()