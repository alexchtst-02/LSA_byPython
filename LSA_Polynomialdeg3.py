import numpy as np
import matplotlib.pyplot as plt

# y = x^3 + 1
data = [
    (-2, -9.02),
    (-1, 5),
    (0, 1.001),
    (1, 2.00001),
    (2, 9),
    (3, 27.98),
    (4, 65),
    (5, 20)
]

xi_6 = 0
xi_5 = 0
xi_4 = 0
xi_3 = 0
xi_2 = 0
xi_1 = 0
xi_3_yi = 0
xi_2_yi = 0
xi_1_yi = 0
yi = 0
n = len(data)

for i in data:
    x = i[0]
    y = i[1]
    xi_6 = xi_6 + (i[0])**6
    xi_5 = xi_5 + (i[0])**5
    xi_4 = xi_4 + (i[0])**4
    xi_3 = xi_3 + (i[0])**3
    xi_2 = xi_2 + (i[0])**2
    xi_1 = xi_1 + (i[0])
    xi_3_yi = xi_3_yi + (i[0]**3)*(i[1])
    xi_2_yi = xi_2_yi + (i[0]**2)*(i[1])
    xi_1_yi = xi_1_yi + (i[0])*(i[1])
    yi = yi + (i[1])
    plt.plot(x, y, 'o')
    
A = np.array([
    (xi_6, xi_5, xi_4, xi_3),
    (xi_5, xi_4, xi_3, xi_2),
    (xi_4, xi_3, xi_2, xi_1),
    (xi_3, xi_2, xi_1, n)
])

r = np.array([
    (xi_3_yi),
    (xi_2_yi),
    (xi_1_yi),
    (yi)
])

koef = np.linalg.solve(A, r)

a = int(data[0][0]) - 5
b = int(data[-1][0]) + 5

yPointsGenerator = lambda x : (koef[0])*(x**3) + (koef[1])*(x**2) + (koef[2])*x + koef[3]

xiteration = ((i) for i in range(a, b))
yiteration = ((yPointsGenerator(i)) for i in range(a, b))

xPoints = np.fromiter(xiteration, dtype=float)
yPoints = np.fromiter(yiteration, dtype=float)

error = 0
for i in data:
    error = error + (yPointsGenerator(i[0]) - i[1])**2

plt.plot(xPoints, yPoints)

print(koef)
print(error)

plt.show()
