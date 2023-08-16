from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


# Main keyboard
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

button_1 = KeyboardButton(text="/help")
button_2 = KeyboardButton(text="/description")
button_3 = KeyboardButton(text="/change_state")
button_4 = KeyboardButton(text="/random")
keyboard.add(button_1).insert(button_2).add(button_3).insert(button_4)


# Inline Rate keyboard
inline_rate_keyboard = InlineKeyboardMarkup(row_width=2)

inline_button_1 = InlineKeyboardButton(text="👍", callback_data="like")
inline_button_2 = InlineKeyboardButton(text="👎", callback_data="dislike")
inline_rate_keyboard.add(inline_button_1, inline_button_2)


# Inline state keyboard
inline_state_keyboard = InlineKeyboardMarkup(row_width=2)

inline_button_3 = InlineKeyboardButton(text="Текущая погода", callback_data="current")
inline_button_4 = InlineKeyboardButton(text="Прогноз погоды", callback_data="forecast")
inline_state_keyboard.add(inline_button_3).add(inline_button_4)