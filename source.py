import networkx as nx
import matplotlib.pyplot as plt


for i in range(10):
    G = nx.generators.random_regular_graph(i, 6)
    nx.draw_circular(G)
    plt.show()