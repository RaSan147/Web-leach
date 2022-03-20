import asyncio
import sys

import pyimgbox

# # Uncomment this to enable debugging messages
import logging
logging.basicConfig(level=logging.DEBUG)


# Using Gallery as an asynchronous context manager is the simplest usage.

async def example1(filepaths):
	async with pyimgbox.Gallery(title="Hello, World!", adult=True) as gallery:
		async for submission in gallery.add(filepaths):
			if not submission['success']:
				print(f"{submission['filename']}: {submission['error']}")
				return False
			else:
				return submission

files = ["./%i.jpg"%i for i in range(1, 10)]

asyncio.run(example1(files))



