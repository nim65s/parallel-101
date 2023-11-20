#!/usr/bin/env python


from concurrent.futures import ProcessPoolExecutor
from time import perf_counter

from task import task


def process_pool(count: int, size: int):
    start = perf_counter()
    with ProcessPoolExecutor() as executor:
        for t in executor.map(task, [size] * count):
            print(t)
    end = perf_counter()

    return end - start


if __name__ == "__main__":
    print("total:", process_pool(20, 5_000))
