from random import randint

def make_grip(n: int, m: int) -> list[list[int]]:
    grip = [[0] * m for i in range(n)]
    for i in range(n):
       if i % 3 == 0:
          for j in range(1, m, 2):
              grip[i][j] = 1
       else:
           for j in range(0, m, 2):
               grip[i][j] = 1
    return grip


def titles(n: int, m: int):
    def generator(i: int, j: int) -> str | None:
        if 0 <= i <= n and 0 <= j <= m:
            return str(i*m + j)
        return None
    return generator


def make_graph(n: int, m: int, add_v_u=False, weights:tuple[int, int]|None=None) -> list[tuple[str, str, int]]:
    result = []
    grip = make_grip(n, m)
    graph = titles(n, m)
    for i in range(n):
        for j in range(m):
            u = graph(i, j)
            V = [
                (i+1, j-1),
                (i+1, j),
                (i,   j+1),
                (i+1, j+1)
            ]
            for vi, vj in V:
                v = graph(vi, vj)
                if v and vi < n and vj < m and grip[i][j] and grip[vi][vj]:
                    w = randint(weights[0], weights[1]) if weights else 1
                    result.append((u, v, w))
                    if add_v_u:
                        result.append((v, u, w))
    return result

