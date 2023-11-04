def make_race_functions(asyncio, awaitable, inspect):
    async def race_functions(*functions):
        @awaitable
        def wrap_sync(i, f):
            result = f()
            return i, result

        async def wrap_async(i, f):
            result = await f()
            return i, result

        done, pending = await asyncio.wait(
            map(
                lambda i, f: asyncio.create_task(
                    wrap_async(i, f) if inspect.iscoroutinefunction(f) else wrap_sync(i, f)
                ),
                *zip(*enumerate(functions))
            ),
            return_when=asyncio.FIRST_COMPLETED
        )

        for task in pending:
            task.cancel()

        return await done.pop()

    return race_functions
