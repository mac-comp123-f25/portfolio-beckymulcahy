import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]

plt.bar(categories, values)

plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Simple Bar Graph')

plt.show()