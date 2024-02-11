from representations import NodeRecord

def from_matrix(matrix: list[list[int | float]],
                labels: list[str],
                target_node: int | str) -> list[str]:
    if isinstance(target_node, str):
        target_node = labels.index(target_node)
    neighbours = []
    n = len(matrix)
    for i in range(n):
        if matrix[i][target_node] > 0 or matrix[target_node][i] > 0:
            neighbours.append(i)
    return [labels[i] for i in neighbours]


def from_edge_list(edges: list[tuple[str, str, int | float]],
                   labels: list[str],
                   target_node: int | str) -> list[str]:
    if isinstance(target_node, int):
        target_node = labels[target_node]
    neighbours = []
    for edge in edges:
        u, v, weight = edge
        if weight > 0 and u != v:
            if target_node == u: neighbours.append(v)
            if target_node == v: neighbours.append(u)
    return neighbours


def from_node_records(nodes: list[NodeRecord], target_node: int | str | NodeRecord):
    if isinstance(target_node, int):
        target_node = nodes[target_node]
    if isinstance(target_node, str):
        target_node = next(filter(lambda nr: nr.title == target_node, nodes))
    return target_node.neighbours


if __name__ == "__main__":
    from data import labels, matrix
    import representations as graphs

    print("Задача нахождения всех соседей заданной вершины графа")

    T = int(input("Количество тестов: "))
    for t in range(T):
        target = input("Имя вершины или индекс (с нуля): ")
        if target.isdigit():
            target = labels[int(target)]

        solve1 = from_matrix(matrix, labels, target)
        print("Решение через матрицу смежности:".ljust(35), solve1)

        edges = graphs.edge_list_from_matrix(matrix, labels)
        solve2 = from_edge_list(edges, labels, target)
        print("Решение через список рёбер:".ljust(35), solve2)

        records = graphs.node_records_from_matrix(matrix, labels)
        solve3 = from_node_records(records, target)
        print("Решение через массив записей:".ljust(35), solve3)

