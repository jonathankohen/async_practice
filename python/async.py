import asyncio


async def main():
    print("yoni")
    task = asyncio.create_task(sleep("hol' up"))
    await asyncio.sleep(0.5)
    print("finished")


async def sleep(text):
    print(text)
    await asyncio.sleep(1)


asyncio.run(main())
