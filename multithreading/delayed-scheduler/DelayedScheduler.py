import asyncio
from typing import Callable


class DelayedScheduler:
    def __init__(self):
        self.tasks = []

    async def schedule(self, delay: int, func: Callable, *args, **kwargs):
        await asyncio.sleep(delay)
        if asyncio.iscoroutinefunction(func):
            await func(*args, **kwargs)
        else:
            await asyncio.to_thread(func(*args, **kwargs))

    async def add_task(self, delay: int, func: Callable, *args, **kwargs):
        task = asyncio.create_task(self.schedule(delay, func, *args, **kwargs))
        self.tasks.append(task)

    async def run(self):
        await asyncio.gather(*self.tasks)
