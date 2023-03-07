import numpy as np
import matplotlib.pyplot as plt


# y = x^2(x^2 - 1)
data = [
    (1, 0.2),
    (2, 11),
    (3, 70),
    (4, 241),
    (5, 592),
    (6, 1200)
]

xi_8 = 0
xi_7 = 0
xi_6 = 0
xi_5 = 0
xi_4 = 0
xi_3 = 0
xi_2 = 0
xi_1  = 0
xi_4_yi = 0
xi_3_yi = 0
xi_2_yi = 0
xi_1_yi = 0
yi_1 = 0
n = len(data)

for i in data:
    x = i[0]
    y = i[1]
    xi_8 = xi_8 + (i[0])**8
    xi_7 = xi_7 + (i[0])**7
    xi_6 = xi_6 + (i[0])**6
    xi_5 = xi_5 + (i[0])**5
    xi_4 = xi_4 + (i[0])**4
    xi_3 = xi_3 + (i[0])**3
    xi_2 = xi_2 + (i[0])**2
    xi_1 = xi_1 + (i[0])**1
    xi_4_yi = xi_4_yi + (i[0]**4)*(i[1])
    xi_3_yi = xi_3_yi + (i[0]**3)*(i[1])
    xi_2_yi = xi_2_yi + (i[0]**2)*(i[1])
    xi_1_yi = xi_1_yi + (i[0])*(i[1])
    yi_1 = yi_1 + (i[1])
    plt.plot(x, y, 'o')
    
A = np.array([
    (xi_8, xi_7, xi_6, xi_5, xi_4),
    (xi_7, xi_6, xi_5, xi_4, xi_3),
    (xi_6, xi_5, xi_4, xi_3, xi_2),
    (xi_5, xi_4, xi_3, xi_2, xi_1),
    (xi_4, xi_3, xi_2, xi_1, n)
])

b = np.array([
    (xi_4_yi),
    (xi_3_yi),
    (xi_2_yi),
    (xi_1_yi),
    (yi_1)
])

koef = np.linalg.solve(A, b)

a = data[0][0] - 5
b = data[-1][0] + 5

yPointsGenerator = lambda x : (koef[0])*x**4 + (koef[1])*x**3 + (koef[2])*x**2 + (koef[3])*x + (koef[4])
my_xiteration = ((i) for i in range(a, b))
my_yiteration = ((ypoints(i)) for i in range(a, b))

error = 0
for i in data:
    error = error + (yPointsGenerator(i[0]) - i[1])**2

xpoints = np.fromiter(my_xiteration, dtype=float)
ypoints = np.fromiter(my_yiteration, dtype=float)
plt.plot(xpoints, ypoints)

print(koef)
print(error)

plt.show()
