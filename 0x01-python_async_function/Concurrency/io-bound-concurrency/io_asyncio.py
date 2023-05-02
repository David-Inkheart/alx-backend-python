#!/usr/bin/env python3
"""
asyncio is a library to write concurrent code using the async/await syntax.
asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.

this is the same code as io_threading.py but using asyncio

runs in 2.5 seconds to 3.5 seconds
"""
import asyncio
import time
import aiohttp


async def download_site(session, url):
    """Async function to download a site"""
    # note the variation of await used here. `async with` is still
    # the same concept of waiting for the response to be returned
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    """Async function to download all sites"""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            # create a list of tasks to be executed
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        # wait for all tasks to be completed
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    # create a list of sites to be downloaded
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    # start the timer
    start_time = time.time()
    # run the async function
    # asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    asyncio.run(download_all_sites(sites))  # a modern way to run
    # calculate the duration
    duration = time.time() - start_time
    # print the result
    print(f"Downloaded {len(sites)} sites in {duration} seconds")
