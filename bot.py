import main

from config import TG_BOT_TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher(bot=bot)


async def on_startup(_):
    print("Bot started")


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет")


@dp.message_handler()
async def get_weather(message: types.Message):
    city = message.text
    reply = main.get_weather(city)
    await message.reply(reply)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
