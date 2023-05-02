#!/usr/bin/env python3
"""
Multiprocessing version of cpu_non_concurrent.py
"""
import multiprocessing
import time


def cpu_bound(number):
    return sum(i * i for i in range(number))

# The find_sums() function is the same as the calculate_sums() function from the previous example. The only difference is that it uses multiprocessing.Pool() to run the cpu_bound() function in parallel. The multiprocessing.Pool() class represents a pool of worker processes. It has methods which can be used to offload tasks to the worker processes and retrieve the results of the tasks. The map() method is one of those methods. It takes a function and an iterable as arguments. It then sends each item in the iterable to the function and returns a list of the results. In this case, the iterable is the numbers list, and the function is cpu_bound(). The map() method sends each number in the numbers list to the cpu_bound() function and returns a list of the results. The multiprocessing.Pool() class takes care of creating the worker processes and distributing the tasks across them. It also takes care of collecting the results from the worker processes and returning them.
# You can specify how many Process objects you want created and managed in the Pool. By default, it will determine how many CPUs are in your machine and create a process for each one. While this works great for our simple example, you might want to have a little more control in a production environment. You can specify the number of processes you want created by passing the processes argument to multiprocessing.Pool(). For example, if you want to create a pool with 4 processes, you can do it like this:
# pool = multiprocessing.Pool(processes=4)


def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


# This takes about 1.2 seconds to run on my machine. That’s about 4 times faster than the non-concurrent version. This is because the multiprocessing.Pool() class creates as many processes as my cpu cores and distributes the tasks across them. Each process runs on a different CPU core, so all are busy at the same time. This is why it is so much faster than the non-concurrent version.

if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
