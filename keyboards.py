from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


# Main keyboard
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

button_1 = KeyboardButton(text="/help")
button_2 = KeyboardButton(text="/description")
button_3 = KeyboardButton(text="/change_state")
button_4 = KeyboardButton(text="/random")
keyboard.add(button_1).insert(button_2).add(button_3).insert(button_4)


# Inline keyboard
inline_keyboard = InlineKeyboardMarkup(row_width=2)

inline_button_1 = InlineKeyboardButton(text="👍", callback_data="like")
inline_button_2 = InlineKeyboardButton(text="👎", callback_data="dislike")
inline_keyboard.add(inline_button_1, inline_button_2)