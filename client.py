import asyncio
import aiohttp

url = 'http://localhost:5000'


@asyncio.coroutine
def fetch(url):
    response = yield from aiohttp.post(url)
    print("content-encoding:", response.headers['content-encoding'])
    return (yield from response.release())

content = asyncio.get_event_loop().run_until_complete(
    fetch(url)
)
print(content)
