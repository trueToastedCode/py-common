import asyncio


async def timeout(future, ms):
    if ms is None or ms <= 0:
        return await future
    return await asyncio.wait_for(future, timeout=ms / 1000)
