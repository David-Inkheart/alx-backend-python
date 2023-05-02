#!/usr/bin/env python3
# countasync.py
"""
Script to demo coroutine with asyncio.
take note of what looks different than if you were to define the
functions with just `def` and `time.sleep()`
"""

import asyncio
import time

# This takes 1 second. And each call of count gets executed in parallel.


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    # await asyncio.gather(count(), count(), count())
    await asyncio.gather(*(count() for _ in range(3)))
    # The asterisk in front of the generator expression is used to unpack the generator expression into positional arguments.

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


"""
# This takes longer, 3seconds. And each call of count gets executed one after the other.
def count():
    print("One")
    time.sleep(1)
    print("Two")


def main():
    count(), count(), count()


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
"""
