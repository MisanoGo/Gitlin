import logging
import asyncio

import aiobot


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(aiobot.fire())
