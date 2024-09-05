from random import random

def get_random_index(weights: list[float]):
    F = [round(sum(weights[:i+1]), 10) for i in range(len(weights))]
    r = random()
    return F.index([f for f in F if r < f][0])


if __name__ == "__main__":
    W = [0.1, 0.1, 0.5, 0.3]
    V = [get_random_index(W) for i in range(1000)]
    for i in range(4):
        print(i, W[i], V.count(i) / 1000)
