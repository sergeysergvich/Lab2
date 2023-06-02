import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

bot = Bot(token="6190585529:AAGK0-RvjHCdYjWbtJTe9ytF34pC1mBIz9Q")
dp = Dispatcher(bot)
kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

b1 = KeyboardButton("/psychologist")
b2 = KeyboardButton("/ophthalmologist")
b3 = KeyboardButton("/neurologist")
b4 = KeyboardButton("/therapist")
kb.add(b1).add(b2).add(b3).add(b4)

CHOICE_DOC = """Нажмите для выбора"""

@dp.message_handler(commands=["start"])
async def cmd_start(msg: types.Message) -> None:
    await msg.answer("Добрый день, для записи на приём введите комманду /login")

    @dp.message_handler(commands=["login"])
    async def cmd_login(msg: types.Message) -> None:
        await msg.answer("Введите ваше ФИО")

        @dp.message_handler()
        async def cmd_choice(msg: types.Message) -> None:
            FIO = str(msg.text)
            #if msg.text.capitalize():
            await bot.send_message(chat_id=msg.from_user.id,
                text="Что бы перейти к выбору врача введите команду /choice",
                parse_mode="HTML")

@dp.message_handler(commands=["choice"])
async def cmd_search(msg: types.Message) -> None:
    await bot.send_message(chat_id=msg.from_user.id,
        text=CHOICE_DOC,
        parse_mode="HTML",
        reply_markup=kb)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)