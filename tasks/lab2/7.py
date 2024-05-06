from challange.tester import Test
from lattices import hexagonal
from algo import prim

import matplotlib.pyplot as plt

X = []; Y = []
N = 80+1
for n in range(10, N):
    graph = hexagonal(n, n)
    test = Test(f"{n}", prim, (graph,))
    X.append(n)
    Y.append(test.run())

plt.plot(X, Y)
plt.xlabel("Размер сетки")
plt.ylabel("Время алгоритма, с")
plt.show()