import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle

from data import matrix, labels
from representations import edge_list_from_matrix

edge_list = edge_list_from_matrix(matrix, labels)
G = nx.DiGraph()

for edge in edge_list:
    u, v, w = edge
    G.add_edge(u, v, weight=w)

marker = MarkerStyle(marker='o', fillstyle='none')
nx.draw_planar(G,
               with_labels=True,
               node_size=600,
               node_shape=marker,
               arrowsize=15,
               node_color='000000')
plt.show()
