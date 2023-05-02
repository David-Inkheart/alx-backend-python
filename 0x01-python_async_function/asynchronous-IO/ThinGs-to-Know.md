# Conclusion

This tutorial equips to use async/await and the libraries built off of it. Here’s a recap of what is covered:

- Asynchronous IO as a language-agnostic model and a way to effect concurrency by letting coroutines indirectly communicate with each other

- The specifics of Python’s new async and await keywords, used to mark and define coroutines

- asyncio, the Python package that provides the API to run and manage coroutines

## Libraries That Work With async/await

### From [aio-libs](https://github.com/aio-libs):

- [aiohttp](https://github.com/aio-libs/aiohttp): Asynchronous HTTP client/server framework

- [aioredis](https://github.com/aio-libs/aioredis-py): Async IO Redis support

- [aiopg](https://github.com/aio-libs/aiopg): Async IO PostgreSQL support

- [aiomcache](https://github.com/aio-libs/aiomcache): Async IO memcached client

- [aiokafka](https://github.com/aio-libs/aiokafka): Async IO Kafka client

- [aiozmq](https://github.com/aio-libs/aiozmq): Async IO ZeroMQ support

- [aiojobs](https://github.com/aio-libs/aiojobs): Jobs scheduler for managing background tasks

- [async_lru](https://github.com/aio-libs/async-lru): Simple [LRU cache](https://realpython.com/lru-cache-python/) for async IO

### From [magicstack](https://magic.io/):

- [uvloop](https://github.com/MagicStack/uvloop): Ultra fast async IO event loop

 -[asyncpg](https://github.com/MagicStack/asyncpg): (Also very fast) async IO PostgreSQL support

### From other hosts:

- [trio](https://github.com/python-trio/trio): Friendlier asyncio intended to showcase a radically simpler design

- [aiofiles](https://github.com/Tinche/aiofiles): Async file IO

- [asks](https://github.com/theelous3/asks): Async requests-like http library

- [asyncio-redis](https://github.com/jonathanslenders/asyncio-redis): Async IO Redis support

- [aioprocessing](https://github.com/dano/aioprocessing): Integrates multiprocessing module with asyncio

- [umongo](https://github.com/Scille/umongo): Async IO MongoDB client

- [unsync](https://github.com/alex-sherman/unsync): Unsynchronize asyncio

- [aiostream](https://github.com/vxgmichel/aiostream): Like itertools, but async