import asyncio
from time import sleep

def basic_function(num):
    sleep(2)
    return num

async def getter_function():
    sleep(1)
    return basic_function()

async def run_my_stuff_now():
    for i in range(10):
        res = await getter_function()
        print(res)

loop = asyncio.get_event_loop()
res = loop.run_until_complete(run_my_stuff_now())