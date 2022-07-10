from aiogram import types
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import logging
import random
import os
import requests
import asyncio
import python_weather

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello, {message.from_user.full_name}!\n"
                           f"My name is Bot,  James Bot.\n"
                           f"Enter a digit to square it up\n"
                           f"Click to /quiz to take a quiz\n"
                           f"Click to /mem to receive a mem\n"
                           f"Click to /EUR to receive EUR/KGS rate\n"
                           f"Click to /weather to receive info about current weather")


@dp.message_handler(commands=['EUR'])
async def eur_handler(message: types.Message):
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url)
    data = response.json()
    data = data.get('rates', {}).get('KGS')
    await bot.send_message(message.from_user.id,
                           f'The actual exchange rate for EUR is {round(data,2)} KGS')



@dp.message_handler(commands=['mem'])
async def mem_sender(message: types.Message):
    list_of_mem = os.listdir('media')
    chosen_mem = random.choice(list_of_mem)
    mem = open(f"media/{chosen_mem}", "rb")
    await bot.send_photo(message.from_user.id, photo=mem)


@dp.message_handler(commands=['weather'])
async def weather_sender(message: types.Message):
    client = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await client.find("Bishkek")
    current_t = (weather.current.temperature - 32) / 1.8
    await client.close()
    await bot.send_message(message.from_user.id,
                           f'Current temperature in Bishkek is {round(current_t, 1)} °C')


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
