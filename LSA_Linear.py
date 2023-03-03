import matplotlib.pyplot as plt
import numpy as np

# the data of (x,y) is a y = 2*x + 1
data = [
    (1, 3),
    (2, 4.2),
    (3, 6),
    (4, 9),
    (5, 13),
    (6,3),
    (7,10),
    (8,14),
    (9,1.2),
    (10,21),
    (11,20),
    (12, 22)
]

# ploting the edges
for i in data:
    x = i[0]
    y = i[1]
    plt.plot(x, y, 'o')

# approximation the linear line
sigma_x_square = 0
sigma_x = 0
sigma_y = 0
sigma_xy = 0
for i in data:
    sigma_x_square = sigma_x_square + (i[0])**2
    sigma_x = sigma_x + (i[0])
    sigma_y = sigma_y + i[1]
    sigma_xy = sigma_xy + i[0]*i[1]
    plt.plot()

n = len(data)

A = np.array([
    (sigma_x_square, sigma_x),
    (sigma_x, n)
])

r = np.array([
    (sigma_xy),
    (sigma_y)
])

koef = np.linalg.solve(A, r)
y0 = koef[0]*data[0][0] + koef[1]
y1 = koef[0]*data[-1][0] + koef[1]
xpoints = np.array([data[0][0], data[-1][0]])
ypoints = np.array([y0, y1])

plt.plot(xpoints, ypoints)
plt.show()

error = 0
for i in data:
    error = error + (ypoints(x) - y)**2
    
print(koef)
print(error)

plt.show()
# this will get us (2.0548, 0.4515)