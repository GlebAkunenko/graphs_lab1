from copy import deepcopy

from representations import NodeRecord


def _parse_to_edges(path: str) -> list[tuple[str, str]]:
    nodes = path.split()
    result = []
    for i in range(len(nodes) - 1):
        result.append((nodes[i], nodes[i+1]))
    return result


def from_matrix(matrix: list[list[int | float]],
                labels: list[str],
                path: str) -> bool:
    edges = _parse_to_edges(path)
    matrix = [m.copy() for m in matrix]
    for edge in edges:
        u, v = edge
        i, j = labels.index(u), labels.index(v)
        if matrix[i][j] == 0:
            return False
        matrix[i][j] = 0
    return True


def from_edge_list(edge_list: list[tuple[str, str, int | float]], path: str) -> bool:
    edge_list = [(u, v) for (u, v, w) in edge_list]
    edges = _parse_to_edges(path)
    for edge in edges:
        if edge not in edge_list:
            return False
        edge_list.remove(edge)
    return True


def from_node_records(nodes: list[NodeRecord], path: str) -> bool:
    nodes = deepcopy(nodes)
    edges = _parse_to_edges(path)
    nodes = {
        node.title: node
        for node in nodes
    }
    for edge in edges:
        u, v = edge
        _from, _to = nodes[u], nodes[v]
        if not _from.is_connected(_to):
            return False
        _from.disconnect(_to)
    return True


if __name__ == "__main__":

    from data import labels, matrix
    import representations as graphs

    print("Задача проверки задаёт ли заданная последовательность вершин цепь")

    T = int(input("Количество тестов: "))
    for t in range(T):
        path = input("Последовательность вершин: ")

        solve1 = from_matrix(matrix, labels, path)
        print("Решение через матрицу смежности:".ljust(35), solve1)

        edges = graphs.edge_list_from_matrix(matrix, labels)
        solve2 = from_edge_list(edges, path)
        print("Решение через список рёбер:".ljust(35), solve2)

        records = graphs.node_records_from_matrix(matrix, labels)
        solve3 = from_node_records(records, path)
        print("Решение через массив записей:".ljust(35), solve3)

