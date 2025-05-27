import matplotlib.pyplot as plt

marks = [12, 54, 35, 68, 89, 97, 23, 46, 71]

plt.hist(marks, bins= 4, rwidth=0.95, color='g')  # -> bins=[0,25,50,75]

plt.show()