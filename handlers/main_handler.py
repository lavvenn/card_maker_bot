from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from aiogram.fsm.context import FSMContext

from keyboards.reply import main_keyboard


router = Router()

WELLCOME_MESSAGE = "Welcome to my bot!"


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(WELLCOME_MESSAGE)