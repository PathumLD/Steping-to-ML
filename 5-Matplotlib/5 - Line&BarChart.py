import matplotlib.pyplot as plt

#   Line

age = [10, 20, 30, 40, 50, 60, 70]
weight = [30, 50, 55, 65, 65, 50, 57]

plt.xlabel('Age')
plt.ylabel('Weight')

plt.plot(age, weight)

plt.show()


#   Bar

subject = ['Maths', 'Physics', 'Chemistry', 'English']
marks = [95, 78, 82, 60]

plt.bar(subject, marks, width=0.4)  #   -> plt.barh(subject, marks, width) -> h = horizontal

plt.show()