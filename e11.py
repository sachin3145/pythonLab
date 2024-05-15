""" write a python program to draw xy axis plot. Add title and legends to the plot """

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = list(map(lambda x:x**2, x))

plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('x squared')
plt.title('square curve')

plt.show()