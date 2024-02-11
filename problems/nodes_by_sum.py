from representations import NodeRecord


def from_matrix(matrix: list[list[int | float]],
                labels: list[str],
                limit: int | float) -> list[str]:
    def sum_of_incidents(node: int):
        result = 0
        n = len(matrix)
        for i in range(n):
            result += matrix[node][i] + matrix[i][node]
        return result

    return [
        labels[i]
        for i in range(len(matrix))
        if sum_of_incidents(i) > limit
    ]



def from_edge_list(edges: list[tuple[str, str, int | float]],
                   labels: list[str],
                   limit: int | float) -> list[str]:
    def sum_of_incidents(node: str):
        result = 0
        for edge in edges:
            u, v, w = edge
            if node in (v, u):
                result += w
        return result

    return [
        labels[i]
        for i in range(len(labels))
        if sum_of_incidents(labels[i]) > limit
    ]


def from_node_records(nodes: list[NodeRecord], limit: int | float) -> list[str]:
    return [
        node.title
        for node in nodes
        if sum(node.incidents_weights) > limit
    ]


if __name__ == "__main__":

    from data import labels, matrix
    import representations

    print("Задача нахождения вершин, сумма весов инцидентных ребер которых больше заданной величины")

    T = int(input("Количество тестов: "))
    for t in range(T):
        limit = float(input("Пороговое значение: "))

        solve1 = from_matrix(matrix, labels, limit)
        print("Решение через матрицу смежности:".ljust(35), solve1)

        edges = graphs.edge_list_from_matrix(matrix, labels)
        solve2 = from_edge_list(edges, labels, limit)
        print("Решение через список рёбер:".ljust(35), solve2)

        records = graphs.node_records_from_matrix(matrix, labels)
        solve3 = from_node_records(records, limit)
        print("Решение через массив записей:".ljust(35), solve3)


