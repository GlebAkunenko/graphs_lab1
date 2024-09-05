import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle

from representations import NodeRecord
from utils import get_random_index, draw_graph

class Node(NodeRecord):
    def __init__(self, id, parent: "Node"):
        super().__init__(id, str(id))
        if parent:
            parent.connect(self)
        self.t = 0

    def update(self):
        self.t += 1

    def p(self, k):
        return self.t ** k


def create_graph(n, k):
    nodes = [Node(0, None)]
    nodes[0].update()

    for i in range(1, n):
        P = [node.p(k) for node in nodes]
        a = 1 / sum(P)
        W = [p * a for p in P]
        index = get_random_index(W)
        parent = nodes[index]
        new = Node(i, parent)
        nodes.append(new)
        [node.update() for node in nodes]

    return nodes


def to_edge_list(nodes: list[NodeRecord]) -> list[tuple[str, str, int | float]]:
    edges = set()
    for node in nodes:
        for child in node.children:
            edges.add((node.title, child, 1))
    return list(edges)

def to_nx(edges: list[tuple[str, str, int]]):
    G = nx.Graph()
    for edge in edges:
        u, v, w = edge
        G.add_edge(u, v, weight=w)
    return G

def draw_graph(edges: list[tuple[str, str, int]]):
    G = to_nx(edges)
    marker = MarkerStyle(marker='o', fillstyle='none')
    plot = nx.draw_spring(G, node_shape=marker, with_labels = True)
    return plot


def draw_degrees(graph: list[Node]):
    D = [node.degree for node in graph]
    plt.hist(D, histtype='step')


# for n in [10, 20, 50]:
#     fig = plt.figure(figsize=(20, 5))
#     for i, k in enumerate([0.1, 0.5, 1, 2]):
#         graph = create_graph(n, k)
#         edges = to_edge_list(graph)
#         ax = plt.subplot(1, 4, i + 1)
#         plt.title(f"n = {n}; k = {k}")
#         draw_graph(edges)
#     plt.savefig(f"{n}.png")

# for n in [10, 20, 50]:
#     fig = plt.figure(figsize=(20, 5))
#     for i, k in enumerate([0.1, 0.5, 1, 2]):
#         graph = create_graph(n, k)
#         ax = plt.subplot(1, 4, i + 1)
#         draw_degrees(graph)
#         plt.title(f"n = {n}; k = {k}")
#     plt.savefig(f"deg_{n}.png")
#     # plt.show()
# #
#
for k in [1, 2, 3, 4]:
    X = []; Y = []
    for n in range(2, 100):
        values = 0; T = 20
        for t in range(T):
            graph: list[Node] = create_graph(n, k)
            d = len([1 for node in graph if len(node.children) > 0])
            values += d
        X.append(n)
        Y.append(values / T)
    plt.plot(X, Y)
    plt.xlabel("размер графа")
    plt.ylabel("среднее количество не листьев")

plt.legend(["k = 1", "k = 2", "k = 3", "k = 4 "])
plt.show()