import matplotlib.pyplot as plt

category = ['Food', 'Transport', 'Rent', 'Drinks', 'Others']
cost = [2300, 4500, 1000, 1200, 3000]

plt.pie(cost, labels=category, radius=1.5, autopct='%0.1f%%', explode=[0, 0.1, 0.2, 0, 0])  #  -> autopct = percentage,  explode = seporate category

plt.show()