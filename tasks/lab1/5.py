from data import matrix, labels
from representations import node_records_from_matrix
from prettytable import PrettyTable

nodes_records = node_records_from_matrix(matrix, labels)

table = PrettyTable([
    "id", "name",
    "P_n", "parents", "P_w",
    "C_n", "children", "C_w",
    "N_n", "neighbours", "N_w",
])

for nr in nodes_records:
    table.add_row((
        nr.id, nr.title,
        len(nr.parents), ", ".join(nr.parents), ", ".join(map(str, nr.input_weights)),
        len(nr.children), ", ".join(nr.children), ", ".join(map(str,nr.output_weights)),
        len(nr.neighbours), ", ".join(nr.neighbours), ", ".join(map(str, nr.incidents_weights)),
    ))

print(table)