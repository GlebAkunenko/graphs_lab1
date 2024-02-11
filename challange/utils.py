from time import time

def measure_func_time(func, *args) -> float:
    sum = 0
    n = 5
    for t in range(n):
        start = time()
        func(*args)
        sum += time() - start
    return sum / n


def make_path(edge_list: list[tuple[str, str, int]], start: str, size: int) -> str:
    offset = 0
    def find_v(u: str):
        nonlocal offset
        for i, edge in enumerate(edge_list[offset:]):
            if edge[0] == u:
                offset = i
                return edge[1]
        return edge_list[offset + 1][0]
    chain: list[str] = []
    offset = 0
    u, v = start, find_v(start)
    while len(chain) < size:
        chain.append(u)
        u, v = v, find_v(v)
    return " ".join(chain)
