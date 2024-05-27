from utils import draw_graph
from lattices import hexagonal
from algo import prim


# n = 15
# m = 10

n = 15
m = 10

graph = hexagonal(n, m, weights=(1, 15))
tree = prim(graph)


draw_graph(graph)
draw_graph(tree)
