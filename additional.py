from data import matrix, labels
from representations import node_records_from_matrix, NodeRecord


def get_sorted_edges(nodes: list[NodeRecord]) -> list[tuple[str, str, int]]:
    edges: list[tuple[str, str, int]] = []
    for node in nodes:
        u = node.title
        for i, v in enumerate(node.children):
            edges.append((u, v, node.output_weights[i]))
    edges.sort(key=lambda e: e[2])
    return edges

nodes = node_records_from_matrix(matrix, labels)
answer = get_sorted_edges(nodes)

for a in answer:
    print(a)
