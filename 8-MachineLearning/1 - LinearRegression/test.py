import numpy as np
import matplotlib.pyplot as plt
import math

y = np.array([1,2,3,4,5])
X = np.array([5,8,11,14,17])

m = 0
b = 0
alpha = 0.1
iteration = 1000
n = len(X)

for i in range(1, 101):
    y_predict = m*X+b

    cost = (1/n) * sum([value ** 2 for value in (y-y_predict)])

    plt.scatter(m, cost)

    dm = -(2/n) * sum(X*(y-y_predict))
    db = -(2/n) * sum(y-y_predict)

    m=m-alpha*dm
    b=b-alpha*db

    print("m {}, c {}, cost {}, iteration {}".format(m, b, cost, i))


plt.show()
