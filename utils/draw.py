import networkx as nx
import matplotlib.pyplot as plt

from matplotlib.markers import MarkerStyle

from lattices.hexagonal import titles

n = 15
m = 10

def draw_graph(edges: list[tuple[str, str, int]]):
    G = nx.Graph()

    node = titles(n, m)
    offset = 0
    positions = {
        node(i, j): (offset + i*10, offset + j*10)
        for i in range(n)
        for j in range(m)
    }

    for edge in edges:
        u, v, w = edge
        G.add_edge(u, v, weight=w)

    marker = MarkerStyle(marker='o', fillstyle='none')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G,
            pos=positions,
            with_labels=True,
            node_size=600,
            node_shape=marker,
            arrowsize=15,
            node_color='000000')
    nx.draw_networkx_edge_labels(G, positions, edge_labels=labels)
    plt.show()


def test():
    G = nx.Graph()

    offset = 0
    positions = {
        "a": (1, 1),
        "b": (1, 5),
        "c": (5, 5),
        "d": (2.5, 2.5),
        "e": (5, 1)
    }

    edges = [
        ("a", "b", 1),
        ("b", "c", 2),
        ("c", "d", 3),
        ("d", "e", 4)
    ]

    for edge in edges:
        u, v, w = edge
        if w > 2:
            G.add_edge(u, v, weight=w)

    marker = MarkerStyle(marker='o', fillstyle='none')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G,
            pos=positions,
            with_labels=True,
            node_size=600,
            node_shape=marker,
            arrowsize=15,
            node_color='000000')
    nx.draw_networkx_edge_labels(G, positions, edge_labels=labels)
    plt.show()


