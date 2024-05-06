from dataclasses import dataclass
from enum import Enum

import problems.all_neighbours
from challange.graphs import matrices, labels
from challange.utils import make_path
from representations import edge_list_from_matrix, node_records_from_matrix
from problems import is_chain, all_neighbours, nodes_by_sum, edge_count
from time import time

def measure(func):
    def _measure(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        return time() - start
    return _measure


class Task(Enum):
    all_neighbours = "Нахождения всех соседей заданной вершины графа"
    is_chain = "Проверка последовательности на определение цепи"
    nodes_by_sum = "Нахождения вершин по сумма весов инцидентных ребер"
    edge_count = "Подсчёт количества ребер в графе"


class Solve(Enum):
    matrix = "матрица смежности"
    edges = "массив рёбер"
    nodes = "массив записей"


@dataclass
class Record:
    task: str
    solve: str
    time: float


def mean(arr: list[int | float]) -> float:
    return sum(arr) / len(arr)


data: list[Record] = []


def test(matrix: list[list[int]], labels: list[str]) -> list[Record]:
    n = len(matrix)
    edge_list = edge_list_from_matrix(matrix, labels)
    node_records = node_records_from_matrix(matrix, labels)
    paths = [
        make_path(edge_list, labels[m], m)
        for m in [1, n // 1000, n // 100, n // 10]
    ]
    result = [
        Record(
            task=Task.all_neighbours.value,
            solve=Solve.matrix.value,
            time=mean([
                measure(problems.all_neighbours.from_matrix)(matrix, labels, x)
                for x in labels[::n // 100]
        ])),
        Record(
            task=Task.all_neighbours.value,
            solve=Solve.edges.value,
            time=mean([
                measure(problems.all_neighbours.from_edge_list)(edge_list, labels, x)
                for x in labels[::n // 100]
            ])
        ),
        Record(
            task=Task.all_neighbours.value,
            solve=Solve.nodes.value,
            time=mean([
                measure(problems.all_neighbours.from_node_records)(node_records, x)
                for x in labels[::n // 100]
            ])
        ),
        Record(
            task=Task.is_chain.value,
            solve=Solve.matrix.value,
            time=mean([
                measure(problems.is_chain.from_matrix)(matrix, labels, path)
                for path in paths
            ])
        ),
        Record(
            task=Task.is_chain.value,
            solve=Solve.edges.value,
            time=mean([
                measure(problems.is_chain.from_edge_list)(edge_list, path)
                for path in paths
            ])
        ),
        Record(
            task=Task.is_chain.value,
            solve=Solve.nodes.value,
            time=mean([
                measure(problems.is_chain.from_node_records)(node_records, path)
                for path in paths
            ])
        ),
        Record(
            task=Task.nodes_by_sum.value,
            solve=Solve.matrix.value,
            time=mean([
                measure(problems.nodes_by_sum.from_matrix)(matrix, labels, limit)
                for limit in [5, 10, 100, 500, 1000]
            ])
        ),
        Record(
            task=Task.nodes_by_sum.value,
            solve=Solve.edges.value,
            time=mean([
                measure(problems.nodes_by_sum.from_edge_list)(edge_list, labels, limit)
                for limit in [5, 10, 100, 500, 1000]
            ])
        ),
        Record(
            task=Task.nodes_by_sum.value,
            solve=Solve.nodes.value,
            time=mean([
                measure(problems.nodes_by_sum.from_node_records)(node_records, limit)
                for limit in [5, 10, 100, 500, 1000]
            ])
        ),
        Record(
            task=Task.edge_count.value,
            solve=Solve.matrix.value,
            time=measure(problems.edge_count.from_matrix)(matrix)
        ),
        Record(
            task=Task.edge_count.value,
            solve=Solve.edges.value,
            time=measure(problems.edge_count.from_edge_list)(edge_list)
        ),
        Record(
            task=Task.edge_count.value,
            solve=Solve.nodes.value,
            time=measure(problems.edge_count.from_node_records)(node_records)
        )
    ]
    return result


from prettytable import PrettyTable

from multiprocessing import Pool

if __name__ == "__main__":
    with Pool() as p:
        records_list = p.starmap(test, [(matrix.copy(), labels.copy()) for matrix in matrices])

    records: dict[tuple[str, str], list[Record]] = {(task.value, solve.value): [] for task in Task for solve in Solve}
    for record in records_list:
        for r in record:
            if isinstance(r, Record):
                records[r.task, r.solve].append(r)
            else:
                raise Exception("")

    tables: list[PrettyTable] = []

    for task in Task:
        table = PrettyTable(field_names=["Представление"] + [f"t{i} (мс)" for i in range(1, len(matrices)+1)], title=task.value)
        table.add_rows([
            [records[task.value, solve.value][0].solve] + [int(records[task.value, solve.value][i].time * 1000) for i in range(len(matrices))]
            for solve in Solve
        ])
        tables.append(table)

    for table in tables:
        print(table)