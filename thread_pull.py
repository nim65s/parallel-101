#!/usr/bin/env python


from concurrent.futures import ThreadPoolExecutor
from time import perf_counter

from task import task


def thread_pool(count: int, size: int):
    start = perf_counter()
    with ThreadPoolExecutor() as executor:
        for t in executor.map(task, [size] * count):
            print(t)
    end = perf_counter()

    return end - start


if __name__ == "__main__":
    print("total:", thread_pool(20, 5_000))
