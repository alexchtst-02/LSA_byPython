import numpy as np
import matplotlib.pyplot as plt
import math

# data = [(t, f)]
data = [
    (0, 1),
    (1/2, -2),
    (1, -5/2),
    (3/2, -1/2),
    (2, 5/4),
    (5/2, -3/2)
]
phi_1 = lambda t : 1
phi_2 = lambda t : math.cos(math.pi*t)
phi_3 = lambda t : math.sin(math.pi*t)

x = 0
y = 0
for i in data:
    x = i[0]
    y = i[1]
    plt.plot(x, y, 'o')

A = np.array([
    (phi_1(data[0][0]), phi_2(data[0][0]), phi_3(data[0][0])),
    (phi_1(data[1][0]), phi_2(data[1][0]), phi_3(data[1][0])),
    (phi_1(data[2][0]), phi_2(data[2][0]), phi_3(data[2][0])),
    (phi_1(data[3][0]), phi_2(data[3][0]), phi_3(data[3][0])),
    (phi_1(data[4][0]), phi_2(data[4][0]), phi_3(data[4][0])),
    (phi_1(data[5][0]), phi_2(data[5][0]), phi_3(data[5][0]))  
])

f = np.array([
    (data[0][1]),
    (data[1][1]),
    (data[2][1]),
    (data[3][1]),
    (data[4][1]),
    (data[5][1])
])

Matrix = np.dot(np.transpose(A), A)

koef = np.linalg.solve(Matrix, (np.dot(np.transpose(A), f)))

a = int(data[0][0]) - 2
b = int(data[-1][0]) + 2

yPointsGenerator = lambda x : koef[0]*1 + koef[1]*math.cos(math.pi*x) + koef[2]*math.sin(math.pi*x)


data_x = []
data_y = []
while a <= b:
    data_x.append(a)
    data_y.append(yPointsGenerator(a))
    a = a + 0.001

error = 0
for i in data:
    error = error + (yPointsGenerator(i[0]) - i[1])**2

xpoints = np.array(data_x, dtype=float)
ypoints = np.array(data_y, dtype=float)

plt.plot(xpoints, ypoints)

print(koef)
print(error)

plt.show()

# masalah x points yang dikeluarkan hanya berupa bilangan bulat saja sehingga tidak terepresentatif dengan baik