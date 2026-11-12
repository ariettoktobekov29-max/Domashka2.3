import asyncio
import logging
from aiogram.fsm.state import State,StatesGroup
from aiogram import F , Router
from aiogram.types import Message, CallbackQuery
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from src.keyboards import keybord_main, inline
from src.questions import QUESTIONS
from src.state import Quiz
from aiogram.fsm.context import FSMContext


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет {message.from_user.full_name}, я твой бот!",
        reply_markup=keybord_main
    )
    print(f"Пользователь {message.from_user.full_name} написал команду /start!")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "/start- команда для запуска\n"
        "/help - список команд\n"
        "/about - узнать подробнее про бота",
        reply_markup=inline 
        
    )


@router.message(Command("about"))
async def cmd_about(message: Message):
    await message.answer(
       "Я — твой новый Telegram-бот.\n"
        "Создан в рамках упорной борьбы с кодом и дедлайнами.\n"
        "Моя главная задача — отвечать на твои сообщения, пока ты думаешь, что бы еще написать."
    )

@router.callback_query(F.data == "quiz_start")
async def quiz_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Начинаем")
    await state.update_data(index=0, score=0)
    await state.set_state(Quiz.waiting_answer)
    await callback.message.answer(f'вопрос:{QUESTIONS[0]['q']}')




@router.message(Quiz.waiting_answer)
async def handle_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    index = data["index"]
    score = data["score"]

    if message.text.lower() == QUESTIONS[index]["a"]:
        score += 1
        await message.answer("Правильно! +1")

    else:
        await message.answer(f"Неверно. Правильный ответ: {QUESTIONS[index]['a']}")

    index += 1
    if index >= len(QUESTIONS):
        await message.answer(f"Конец! Счет: {score}/{len(QUESTIONS)}")
        await state.clear()
    else:
        await state.update_data(index=index, score=score)
        await message.answer(f"вопрос{index +1}: {QUESTIONS[index]['q']}")

# @dp.message(F.from_user.id == 1288365917)
# async def cmd_group(message: Message):
#     await message.answer("Привет мой создатель!!!")
































@router.message(F.text.casefold() == "каталог")
async def cmd_catalog(message: Message):
    await message.answer("Наш каталог к сожалению пуст:(")

@router.message(F.text.casefold() == "пока")
async def cmd_bye(message:Message):
    await message.answer("прощай надеюсь еще увидимся!")


@router.message(F.text.casefold() == "проверка")
async def cmd_goida(message: Message):
    await message.answer("проверка")
    
# @dp.message(F.from_user.id == 1288365917)
# async def cmd_group(message: Message):
#     await message.answer("Привет мой создатель!!!")


@router.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")


   # отправляет запросы на тг-сервер


