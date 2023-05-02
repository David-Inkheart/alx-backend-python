#!/usr/bin/env python3
"""Script to demonstrate CPU bound tasks without concurrency."""

import time


def cpu_bound(number):
    return print(sum(i * i for i in range(number)))


def calculate_sums(numbers):
    for number in numbers:
        cpu_bound(number)


# This code calls cpu_bound() 20 times with a different large number each time. It does all of this on a single thread in a single process on a single CPU core. The CPU is busy the entire time, and the program takes about 5.5 to 5.8 seconds to run on my machine.

# rewiriting the code to use concurrency with threading or asyncio will not make it run faster. In fact, it will make it run slower. This is because of the Global Interpreter Lock (GIL). The GIL prevents Python from running multiple threads in parallel. It only allows Python to run one thread at a time. This means that the CPU is still busy the entire time, but it is only running one thread at a time.

# This is where multiprocessing comes in. Multiprocessing allows Python to run multiple processes in parallel. Each process runs in its own Python interpreter and memory space, so memory is not shared between processes. This means that the GIL won’t be a problem for CPU-bound tasks in multiprocessing. check cpu_mp.py for the multiprocessing version of this code.

if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    calculate_sums(numbers)
    duration = time.time() - start_time

    print(f"Duration {duration} seconds")
