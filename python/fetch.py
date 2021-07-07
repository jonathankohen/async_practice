import asyncio


async def fetch():
    print("fetching...")
    await asyncio.sleep(2)
    print("retrieved.")
    return {"data": 1}


async def print_nums():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)


async def main():
    task = asyncio.create_task(fetch())
    task2 = asyncio.create_task(print_nums())

    value = await task
    print(value)
    await task2


asyncio.run(main())



