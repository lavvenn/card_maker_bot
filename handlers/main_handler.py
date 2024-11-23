from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from aiogram.fsm.context import FSMContext

from keyboards.reply import main_kb


router = Router()

WELLCOME_MESSAGE = "Welcome to my bot!"


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(WELLCOME_MESSAGE, reply_markup=main_kb)


@router.message(F.text == "ℹ️ информация")
async def info(message: Message):
    await message.answer("это бот в разработке")

@router.message(F.text == "/my_id")
async def my_id(message: Message, state: FSMContext):
    await message.answer(message.from_user.id)