#!/usr/bin/env python
import asyncio
from time import perf_counter

import httpx

URL = "https://www.upssitech.eu/"


async def download(client, url):
    try:
        await client.get(url)
    except Exception:
        pass


async def async_web() -> float:
    content = httpx.get(URL).content.decode()
    urls_simple = [url for url in content.split("'") if url.startswith(URL)]
    urls_double = [url for url in content.split('"') if url.startswith(URL)]
    urls = set(url.split()[0] for url in urls_simple + urls_double)

    start = perf_counter()
    async with httpx.AsyncClient() as client:
        await asyncio.gather(*[download(client, url) for url in urls])
    end = perf_counter()

    return end - start


if __name__ == "__main__":
    print("total:", asyncio.run(async_web()))
