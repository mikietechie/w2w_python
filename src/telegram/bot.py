"""
Desc: Telegram bot
"""

from aiogram import (
    Bot,
    Dispatcher,
    types,
)
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from shared import config
from shared.logger import logger
from .routers import (
    start,
    patients,
)


bot = Bot(
    token=config.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML"),
)
storage = MemoryStorage()
dispatcher = Dispatcher(storage=storage)


async def bootstrap_bot():
    """
    Starts the Bot
    """
    logger.info("Bootstrap bot")
    patients.dispatcher.attach(dispatcher)
    dispatcher.include_routers(
        start.router,
        patients.router,
    )
    await bot.set_my_commands(
        [
            types.BotCommand(
                command="/start",
                description="Start",
            ),
            *[
                types.BotCommand(
                    command=f"/{cmd.command}",
                    description=cmd.description,
                )
                for cmd in patients.COMMANDS
            ],
        ]
    )
    await dispatcher.start_polling(bot)
