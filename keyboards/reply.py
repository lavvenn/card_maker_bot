from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 отпрвить данные на пропуск")],
        [KeyboardButton(text="ℹ️ информация")]
    ]
 , resize_keyboard=True)

rm_kb = ReplyKeyboardRemove()