# -*- coding: utf-8 -*-
"""HW1_Question1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15FxhQPV6sMrns2X6mbCFNxoeecpezAw-
"""

import numpy as np
from scipy.signal import argrelextrema
from sympy import *
import matplotlib.pyplot as plt

np.random.seed(420)

# xs = np.random.rand(100, 1)
x = np.linspace(0, 10, 1000)
dx = x[1] - x[0]
y = x**2 + 1
dydx = np.gradient(y, dx)


# ys = xs ** 2 + 2 * xs + np.random.rand(100, 1)


# plt.plot(xs, ys, 'b.')
# plt.show()

# local_min = ys[argrelextrema(ys, np.greater)[0]]
# print(local_min)

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, dydx)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('dydx')

plt.show()

# local_min = np.minimum(xs, ys)
# print(local_min)

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');