from asyncio import run


async def g():
    yield 1


async def main():
    print(anext(g()))


if __name__ == "__main__":
    run(main())
