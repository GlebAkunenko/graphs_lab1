from time import time
import problems


def measure_func_time(func, *args) -> float:
    sum = 0
    n = 2
    for t in range(n):
        start = time()
        func(args)
        sum += time() - start
    return sum / n


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
