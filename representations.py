from dataclasses import dataclass

def edge_list_from_matrix(matrix: list[list[int | float]], labels: list[str]) -> list[tuple[str, str, int | float]]:
    result = []
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                result.append((labels[i], labels[j], matrix[i][j]))
    return result


class NodeRecord:
    def __init__(self, id: int, title: str = None):
        self.id = id
        if title is None:
            title = str(self.id)
        self.title = title
        self.parents: list[str] = []
        self.children: list[str] = []
        self.input_weights: list[int | float] = []
        self.output_weights: list[int | float] = []

    def connect(self, end: "NodeRecord", weight: int | float = 1):
        self.children.append(end.title)
        self.output_weights.append(weight)
        end.parents.append(self.title)
        end.input_weights.append(weight)

    def is_connected(self, with_node: "NodeRecord") -> bool:
        return with_node.title in self.children

    def disconnect(self, another: "NodeRecord"):
        atr_index = self.children.index(another.title)
        del self.children[atr_index]
        del self.output_weights[atr_index]
        slf_index = another.parents.index(self.title)
        del another.parents[slf_index]
        del another.input_weights[slf_index]

    @property
    def neighbours(self) -> list[str]:
        return self.parents + self.children

    @property
    def incidents_weights(self) -> list[int | float]:
        return self.input_weights + self.output_weights

    @property
    def degree(self) -> int:
        return len(self.neighbours)


def node_records_from_matrix(matrix: list[list[int | float]], labels: list[str] = None) -> list[NodeRecord]:
    nodes: list[NodeRecord]
    n = len(matrix)
    if labels is None:
        nodes = [NodeRecord(i) for i in range(n)]
    else:
        nodes = [NodeRecord(i, labels[i]) for i in range(n)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                nodes[i].connect(nodes[j], matrix[i][j])

    return nodes
