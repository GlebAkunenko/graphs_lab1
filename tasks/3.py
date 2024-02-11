from data import matrix, labels
from representations import edge_list_from_matrix

edge_list = edge_list_from_matrix(matrix, labels)

for e in edge_list:
    print(e)