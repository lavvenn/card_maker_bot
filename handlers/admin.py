from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from aiogram.fsm.context import FSMContext

from config import ADMINS_LIST

from keyboards.inline import admin_panel_kb
from keyboards.builders import get_all_cards_keyboard

router = Router()


@router.message(F.text == "/admin", F.from_user.id.in_(ADMINS_LIST))
async def admin(message: Message, state: FSMContext):
    await message.answer("🅰Админ панель🅰", reply_markup=admin_panel_kb)

@router.callback_query(F.data == "check_cards")
async def check_cards(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("выберите человека",reply_markup=get_all_cards_keyboard())

@router.callback_query(F.data == "back_to_admin")
async def back_to_admin(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("🅰Админ панель🅰", reply_markup=admin_panel_kb)