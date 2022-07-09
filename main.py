from aiogram import types
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import logging
import random
import os


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello, {message.from_user.full_name}!\n"
                           f"My name is Bot,  James Bot.\n"
                           f"Enter a digit to square it up\n"
                           f"Click to /quiz to take a quiz\n"
                           f"Click to /mem to receive a mem")


@dp.message_handler(commands=['mem'])
async def mem_sender(message: types.Message):
    list_of_mem = os.listdir('media')
    chosen_mem = random.choice(list_of_mem)
    mem = open(f"media/{chosen_mem}", "rb")
    await bot.send_photo(message.from_user.id, photo=mem)


@dp.message_handler(commands=['quiz'])
async def quiz_handler(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "How many planets are there in the solar system?"
    answers = [
        '7', "8", "9", "10"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Think well",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    # markup.add(button_call_2)

    question = "Which planet in the solar system is closest to the sun?"
    answers = [
        "Earth",
        "Mars",
        "Mercury",
        "Saturn"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Think well",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


@dp.message_handler()
async def echo(message: types.Message):
    try:
        current_message = int(message.text)
        await bot.send_message(message.from_user.id, current_message ** 2)
    except:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)