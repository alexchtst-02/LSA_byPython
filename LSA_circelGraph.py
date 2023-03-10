import numpy as np
import matplotlib.pyplot as plt
import math


# contoh fungsi (x-1)^2 + y^2 = 4

data = [
    (1, 2),
    (1, -2),
    (-1, 0),
    (0, math.sqrt(3))
]

phi_1 = lambda x : x
phi_2 = lambda x : 1



for i in data:
    x = i[0]
    y = i[1]
    plt.plot(x,y,'o')

A = np.array([
    (phi_1(data[0][0]), phi_1(data[0][1]), phi_2(data[0][0])),
    (phi_1(data[1][0]), phi_1(data[1][1]), phi_2(data[1][0])),
    (phi_1(data[2][0]), phi_1(data[2][1]), phi_2(data[2][0])),
    (phi_1(data[3][0]), phi_1(data[3][1]), phi_2(data[3][0]))
])

A_transpose = np.transpose(A)

f = np.array([
    (-((data[0][0])**2 + (data[0][1])**2)),
    (-((data[1][0])**2 + (data[1][1])**2)),
    (-((data[2][0])**2 + (data[2][1])**2)),
    (-((data[3][0])**2 + (data[3][1])**2))
])

koef = np.linalg.solve(np.dot(A_transpose, A), np.dot(A_transpose, f))

print(koef)
# x^2 + Ax + (y^2+ By + c) = 0
determinant = lambda y : (koef[0])**2 - 4*(y**2 + koef[1]*y + koef[2])

a = -5
b = 5
data_x = []
data_y1 = []
data_y2 = []
while a <= b:
    if determinant(a) >= 0:
        ypositif = (-koef[0] + math.sqrt(determinant(a)))/2
        ynegatif = (-koef[0] - math.sqrt(determinant(a)))/2
        data_x.append(a)
        data_y1.append(ypositif)
        data_y2.append(ynegatif)
    a = a + 0.001


xpoints = np.array(data_x)
ypositifpoints = np.array(data_y1)
ynegatifpoints = np.array(data_y2)

plt.plot(xpoints, ynegatifpoints)
plt.plot(xpoints, ypositifpoints)

plt.show()