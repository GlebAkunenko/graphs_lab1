from utils import measure_func_time
from .graphs import matrices, labels
from ..representations import edge_list_from_matrix, node_records_from_matrix

import problems

class Test:
    def __init__(self, task_name: str, task_func, args: list):
        self.task_name = task_name
        self.task_func = task_func
        self.args = args

    def run(self) -> float:
        ans = 0
        n = len(self.args)
        for i, args in enumerate(self.args):
            ans += measure_func_time(self.task_func, *args)
            print(self.task_name, f"{int((i+1) / n * 100)}%")
        return ans / n
