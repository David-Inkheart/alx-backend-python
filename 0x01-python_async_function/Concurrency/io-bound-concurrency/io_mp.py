#!/usr/bin/env python
"""
multiprocessing version of io.py
"""
import multiprocessing
import requests
import time


session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")

# the multiprocessing.Pool class represents a pool of worker processes. It has methods which allows tasks to be offloaded to the worker processes in a few different ways. By default, the Pool creates worker processes equal to the number of CPUs available on the host machine. This is often the right balance between not having too many processes, and not having too few processes to take advantage of all the available CPU resources.


# i had 6 cores and 6 threads and it took 5.5 to 5.9 seconds
def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
