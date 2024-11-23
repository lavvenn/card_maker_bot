import os

from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton


def get_all_cards_keyboard():
    builder = InlineKeyboardBuilder()

    all_cards = os.listdir("output/")

    def delete_prefix(text):
        return text.split(".")[0]

    map(delete_prefix, all_cards)

    for card in all_cards:
        builder.row(
            InlineKeyboardButton(text=card, callback_data=card))

    builder.row(
        InlineKeyboardButton(text="👈назад👈", callback_data="back_to_admin"))

    return builder.as_markup()