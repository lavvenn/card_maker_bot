from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

course_select_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "1️⃣", callback_data="1")],
    [InlineKeyboardButton(text = "2️⃣", callback_data="2")],
    [InlineKeyboardButton(text = "3️⃣", callback_data="3")],
    [InlineKeyboardButton(text = "4️⃣", callback_data="4")],
])

confirmation_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "✅", callback_data="yes")],
    [InlineKeyboardButton(text = "❌", callback_data="no")]
])


admin_panel_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "📝 посмотреть карточки 📝", callback_data="check_cards")],
    [InlineKeyboardButton(text = "📈получить статистику📉", callback_data="check_stats")]
])