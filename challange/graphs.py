from random import random, randint, seed
from time import time

def random_weight(p_zero, max_w):
    if random() < p_zero:
        return randint(1, max_w)
    return 0

n = 10 ** 2 * 2

start = time()

matrices = [
    [
        [
            random_weight(p, 1000)
            for j in range(n)
        ]
        for i in range(n)
    ]
    for p in [0.001, 0.25, 0.5, 1]
]

labels = [str(i+1) for i in range(n)]


