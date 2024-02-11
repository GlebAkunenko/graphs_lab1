from prettytable import PrettyTable
from representations import *

data = [[ 0, 1, 1, 0, 0, 0, 2, 0],
        [ 0, 0, 1, 0, 2, 0, 1, 0],
        [ 0, 0, 0, 0, 5, 0, 0, 0],
        [ 4, 0, 0, 0, 0, 0, 3, 2],
        [ 0, 0, 0, 0, 0, 12, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 5, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0]]


matrix = [d.copy() for d in data]

labels = [f"x{i}" for i in range(1, 8+1)]
data.insert(0, ['x'] + labels)
for i in range(1, len(data)):
    data[i].insert(0, labels[i-1])

if __name__ == "__main__":
    table = PrettyTable(header=False, border=False)
    table.add_rows(data)
    print(table)



