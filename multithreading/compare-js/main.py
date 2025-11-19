import asyncio


async def wait_time_task():
    await asyncio.sleep(2)
    return "completed_text"


async def promise_all():
    tasks = [wait_time_task() for _ in range(5)]
    results = await asyncio.gather(*tasks)
    return results


async def promise_all_settled():
    tasks = [wait_time_task() for _ in range(5)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results
