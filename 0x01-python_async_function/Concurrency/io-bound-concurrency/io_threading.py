#!/usr/bin/env python3

"""
Threading version for the downloading of urls
"""
import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print("Read {} from {}".format(len(response.content), url))


"""Play with number of threads to see the difference and the impact on 
the performance... between 15 and 20 threads is the best for this example and it gives 3.6 seconds tp 4.1 seconds"""


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=19) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
