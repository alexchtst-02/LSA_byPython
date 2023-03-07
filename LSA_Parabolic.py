import matplotlib.pyplot as plt
import numpy as np

# data observation
data = [
    (-5, -30),
    (-4, -20),
    (-3, -12),
    (-2, 1.9),
    (-1, 0),
    (0, -0.9),
    (1, 0.5),
    (2, 5),
    (3, 10),
    (4, 19.6),
    (5, 27),
    (6, 41),
    (7, 55),
    (10, 109.09)
]

# ploting the points from data observation
for i in data:
    x = i[0]
    y = i[1]
    plt.plot(x, y, 'o')

# solving for the parabolic koef
xi_4 = 0
xi_3 = 0
xi_2 = 0
xi = 0
xi_2yi = 0
xiyi = 0
yi = 0
n = len(data)
x_only = []
for i in data:
    x_only.append(i[0])
    xi_4 = xi_4 + (i[0])**4
    xi_3 = xi_3 + (i[0])**3
    xi_2 = xi_2 + (i[0])**2
    xi = xi + i[0]
    xi_2yi = xi_2yi + ((i[0])**2)*i[1]
    xiyi = xiyi + i[0]*i[1]
    yi = yi + i[1]

A = np.array([
    (xi_4, xi_3, xi_2),
    (xi_3, xi_2, xi),
    (xi_2, xi, n)
])

r = np.array([
    (xi_2yi),
    (xiyi),
    (yi)
])

koef = np.linalg.solve(A, r)
y0 = koef[0]*(data[0][0]**2) + koef[1]*data[0][0] + koef[2]
y1 = koef[0]*(data[-1][0]**2) + koef[1]*data[-1][0] + koef[2]

yPointsGenerator = lambda x : (koef[0])*x**2 + (koef[1])*x + (koef[2])

my_yiteration = ((koef[0]*x*x + koef[1]*x + koef[2]) for x in range(-10, 13))
my_xiteration = ((x) for x in range(-10, 13))
xpoints = np.fromiter(my_xiteration, dtype=float)
ypoints = np.fromiter(my_yiteration, dtype=float)

error = 0
for i in data:
    error = error + (yPointsGenerator(i[0]) - i[1])**2

plt.plot(xpoints, ypoints)

print(koef)
print(error)

plt.show()
