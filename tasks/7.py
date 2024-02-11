from sys import getsizeof

from data import matrix, labels
from representations import edge_list_from_matrix, node_records_from_matrix

edge_list = edge_list_from_matrix(matrix, labels)
node_records = node_records_from_matrix(matrix, labels)

print("Объем памяти в байтах для")

print("матрицы".ljust(16), f"{getsizeof(matrix) + getsizeof(labels)}")
print(f"списка рёбер".ljust(16), f"{getsizeof(edge_list)}")
print(f"массив записей".ljust(16), f"{getsizeof(node_records)}")
