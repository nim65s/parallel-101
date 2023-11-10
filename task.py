#!/usr/bin/env python

from time import perf_counter

import numpy as np


def task(size: int) -> int:
    a = np.random.rand(size, size)
    b = np.random.rand(size)

    start = perf_counter()
    np.linalg.solve(a, b)
    end = perf_counter()

    return end - start
