"""
Desc: Main file
"""

import asyncio

from database.mongo import init_async_db
from telegram.bot import bootstrap_bot


async def main():
    """
    Initialises database and starts telegram pooling.
    """
    await init_async_db()
    await bootstrap_bot()


if __name__ == "__main__":
    asyncio.run(main())
