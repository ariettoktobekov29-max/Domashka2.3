import asyncio
import logging
from aiogram import F
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from src.handlers import router

BOT_TOKEN = "8683342969:AAH_0vmddCWse7RBJE4Q-l1MjoqmATB2AFQ"


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()     # обработчик входящих обновлений


# @dp.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.answer(
#         f"Привет {message.from_user.full_name}, я твой бот!"
#     )
#     print(f"Пользователь {message.from_user.full_name} написал команду /start!")


# @dp.message(Command("help"))
# async def cmd_help(message: Message):
#     await message.answer(
#         "/start - команда для запуска\n"
#         "/help - список команд\n"
#         "/about - узнать подробнее про бота"
#     )


# @dp.message(Command("about"))
# async def cmd_about(message: Message):
#     await message.answer(
#        "Я — твой новый Telegram-бот.\n"
#         "Создан в рамках упорной борьбы с кодом и дедлайнами.\n"
#         "Моя главная задача — отвечать на твои сообщения, пока ты думаешь, что бы еще написать."
#     )


    

# @dp.message(F.text.casefold() == "группа")
# async def cmd_group(message: Message):
#     await message.answer("Твоя группа 71-1!")

# @dp.message(F.text.casefold() == "пока")
# async def cmd_bye(message:Message):
#     await message.answer("прощай надеюсь еще увидимся!")


# @dp.message(F.text.casefold() == "гойда")
# async def cmd_goida(message: Message):
#     await message.answer("русский слоняраааа")
    
# # @dp.message(F.from_user.id == 1288365917)
# # async def cmd_group(message: Message):
# #     await message.answer("Привет мой создатель!!!")


# @dp.message()
# async def echo(message: Message):
#     await message.answer(f"Ты написал: {message.text}")


async def main():
    dp.include_router(router=router)
    await dp.start_polling(bot)
         # отправляет запросы на тг-сервер


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
