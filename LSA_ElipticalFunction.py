import numpy as np
import matplotlib.pyplot as plt
import math 


# persamaan umum eliptical y^2 + c1x^2 + c2xy + c3x + c4y + c5 = 0
# y^2 + (c2x+c4)y + c3x + c5 + c1x^2 = 0
data = [
    (1.27, 5.35),
    (5, 5.6),
    (5, 1),
    (-2, -1.5),
    (-1, 2),
    (1.8, -1.5)
]

phi_1 = lambda x : x**2 # untuk c1
phi_2 = lambda x,y : x*y # untuk c2
# phi_3 dan phi_4 adalah fungsi yang sama, namun ditulis dua duanya supaya tidak kesulitan dalam mengolah matrix
phi_3 = lambda x : x # untuk c3
phi_4 = lambda y : y # untuk c4
phi_5 = lambda x : 1 # untuk c5

for i in data:
    x = i[0]
    y = i[1]
    plt.plot(x, y, 'o')

A = np.array([
    (phi_1(data[0][0]), phi_2(data[0][0], data[0][1]), phi_3(data[0][0]), phi_4(data[0][1]), phi_5(data[0][0])),
    (phi_1(data[1][0]), phi_2(data[1][0], data[1][1]), phi_3(data[1][0]), phi_4(data[1][1]), phi_5(data[1][0])),
    (phi_1(data[2][0]), phi_2(data[2][0], data[2][1]), phi_3(data[2][0]), phi_4(data[2][1]), phi_5(data[2][0])),
    (phi_1(data[3][0]), phi_2(data[3][0], data[3][1]), phi_3(data[3][0]), phi_4(data[3][1]), phi_5(data[3][0])),
    (phi_1(data[4][0]), phi_2(data[4][0], data[4][1]), phi_3(data[4][0]), phi_4(data[4][1]), phi_5(data[4][0])),
    (phi_1(data[5][0]), phi_2(data[5][0], data[5][1]), phi_3(data[5][0]), phi_4(data[5][1]), phi_5(data[5][0]))
])

A_Transpose = np.transpose(A)

f = np.array([
    (-(data[0][1])**2),
    (-(data[1][1])**2),
    (-(data[2][1])**2),
    (-(data[3][1])**2),
    (-(data[4][1])**2),
    (-(data[5][1])**2),
])

koef = np.linalg.solve(np.dot(A_Transpose, A), np.dot(A_Transpose, f))
c1 = koef[0]
c2 = koef[1]
c3 = koef[2]
c4 = koef[3]
c5 = koef[4]

a = -6
b = 6
data_x = []
data_y1 = []
data_y2 = []

# y^2 + (c2x+c4)y + c3x + c5 + c1x^2 = 0
determinanant = lambda x: (c2*x + c4)**2 - 4*(c3*x + c5 + c1*(x)**2)
while a <= b:
    if determinanant(a) >= 0:
        y1 = (-(c2*a + c4) + math.sqrt(determinanant(a)))/2
        y2 = (-(c2*a + c4) - math.sqrt(determinanant(a)))/2
        data_x.append(a)
        data_y1.append(y1)
        data_y2.append(y2)
    a = a + 0.001


xpoints = np.array(data_x)
y1_points = np.array(data_y1)
y2_points = np.array(data_y2)

plt.plot(xpoints, y1_points)
plt.plot(xpoints, y2_points)


plt.show()
