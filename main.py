import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

from commands import FILMS_COMMAND

from data import get_films
from keyboards import films_keyboard_markup


load_dotenv()

TOKEN: str = os.getenv("TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Вітаю, {html.bold(message.from_user.full_name)}!\n"
                         f"Я перший бот, Python розробника - Микити Охріменка")


@dp.message(FILMS_COMMAND)
async def command_start_handler(message: Message) -> None:
    data = get_films()
    markup = films_keyboard_markup(films_list=data)

    await message.answer(f"Перелік фільмів. Натисність на назву для отримання деталей", reply_markup=markup)


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
