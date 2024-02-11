from representations import NodeRecord

def from_matrix(matrix: list[list[int | float]]) -> int:
    answer = 0
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            answer += matrix[i][j] > 0
    return answer


def from_edge_list(edge_list: list[tuple[str, str, int | float]]) -> int:
    return len(edge_list)


def from_node_records(nodes: list[NodeRecord]) -> int:
    return sum([
        len(node.output_weights)
        for node in nodes
    ])


if __name__ == "__main__":

    from data import labels, matrix
    import representations

    print("Задача подсчёта количества ребер в графе")

    solve1 = from_matrix(matrix)
    print("Решение через матрицу смежности:".ljust(35), solve1)

    edges = graphs.edge_list_from_matrix(matrix, labels)
    solve2 = from_edge_list(edges)
    print("Решение через список рёбер:".ljust(35), solve2)

    records = graphs.node_records_from_matrix(matrix, labels)
    solve3 = from_node_records(records)
    print("Решение через массив записей:".ljust(35), solve3)

