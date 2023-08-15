import main

from aiogram import Bot, Dispatcher, executor, types
from config import TG_BOT_TOKEN, HELP_COMMAND, DESCRIPTION
from keyboards import keyboard, inline_keyboard
from states import BotStates


bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher(bot=bot)


calls_count = 0
current_state = BotStates.normal


async def on_startup(_):
    print("Bot started")


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожаловать! ✋",
                           reply_markup=keyboard)

    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker="CAACAgIAAxkBAAEKCJlk27-e0PBMTIqy9S9rWKsqKjM96QACBRwAAj4w2EmcRFzWNmiC1zAE")

    await message.delete()


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML")

    await message.delete()


@dp.message_handler(commands=["description"])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=DESCRIPTION,
                           parse_mode="HTML")

    await message.delete()


@dp.message_handler(commands="random")
async def random_weather_command(message: types.Message):
    reply = main.get_weather_in_random_city()
    await bot.send_message(chat_id=message.from_user.id,
                           text=reply,
                           parse_mode="HTML")

    await message.delete()


@dp.message_handler(commands="change_state")
async def change_state(message: types.Message):
    # TODO: weather in random location
    await message.delete()


@dp.message_handler()
async def get_weather(message: types.Message):
    global calls_count
    calls_count += 1

    city = message.text
    reply = main.get_weather(city)
    await bot.send_message(chat_id=message.from_user.id,
                           text=reply,
                           parse_mode="HTML")

    if calls_count % 4 == 0:
        await bot.send_photo(chat_id=message.from_user.id,
                             caption="Тебе нравится пользоваться моим ботом? 😉",
                             photo="https://gas-kvas.com/uploads/posts/2023-02/1675468566_gas-kvas-com-p-zakat-fonovii-risunok-36.jpg",
                             reply_markup=inline_keyboard)


@dp.callback_query_handler()
async def query_handler(callback: types.CallbackQuery):
    if callback.data == "like":
        await callback.answer("Тебе понравился мой бот 😊")
    else:
        await callback.answer("Тебе не понравился мой бот 😢")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
