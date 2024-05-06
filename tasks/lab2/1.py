import networkx as nx
import matplotlib.pyplot as plt

from matplotlib.markers import MarkerStyle

from lattices import hexagonal
from lattices.hexagonal import titles

n = 15
m = 10

graph = hexagonal(n, m)
G = nx.DiGraph()

node = titles(n, m)
offset = 0
positions = {
    node(i, j): (offset + i*300, offset + j*10)
    for i in range(n)
    for j in range(m)
}

for edge in graph:
    u, v, w = edge
    G.add_edge(u, v)

marker = MarkerStyle(marker='o', fillstyle='none')
nx.draw(G,
        pos=positions,
        with_labels=True,
        node_size=600,
        node_shape=marker,
        arrowsize=15,
        node_color='000000')
plt.show()
