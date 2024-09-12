"""
Desc: Start Routes
"""

from aiogram import (
    types,
    filters,
    Router,
)

router = Router(name=__name__)


@router.message(filters.CommandStart())
async def cmd_start(message: types.Message):
    """Start cmd handler"""
    await message.reply(
        text=f"Hello {message.from_user.username}",
        reply_markup=types.ReplyKeyboardRemove(),
    )
