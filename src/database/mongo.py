"""
Desc: Mongo DB Connection
"""

from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from shared import config
from shared.logger import logger
from .documents import DOCUMENT_MODELS


async def init_async_db():
    """
    Connect to DB
    """
    logger.info("Bootstrap bot")
    client = AsyncIOMotorClient(config.MONGO_URI)
    await init_beanie(
        database=client.db_name,
        document_models=DOCUMENT_MODELS,
    )
