import os
import random
import requests
import python_weather
from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from keyboards import client_kb
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from handlers import fsm_menu
from database.bot_db import select_dish_random_sql


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Hello, {message.from_user.full_name}! "
                           f"My name is Bot, James Bot.\n",
                           # f"Enter a digit to square it up\n"
                           # f"Click to /quiz to take a quiz\n"
                           # f"Click to /mem to receive a mem\n"
                           # f"Click to /EUR to receive EUR/KGS rate\n"
                           # f"Click to /weather to receive info about current weather"
                           reply_markup=client_kb.start_makrup)


async def currencies_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Choose the currency',
                           reply_markup=client_kb.currency_markup)


# @dp.message_handler(commands=['EUR'])
async def eur_handler(message: types.Message):
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url)
    data = response.json()
    data = data.get('rates', {}).get('KGS')
    await bot.send_message(message.from_user.id,
                           f'The actual exchange rate for EUR is {round(data,2)} KGS')


# @dp.message_handler(commands=['EUR'])
async def usd_handler(message: types.Message):
    pass
    # url = 'https://api.exchangerate.host/latest'
    # response = requests.get(url)
    # data = response.json()
    # data = data.get('rates', {}).get('KGS')
    # await bot.send_message(message.from_user.id,
    #                        f'The actual exchange rate for EUR is {round(data,2)} KGS')


# @dp.message_handler(commands=['weather'])
async def weather_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Choose the city',
                           reply_markup=client_kb.weather_markup)


async def fru_sender(message: types.Message):
    client = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await client.find("Bishkek")
    current_t = (weather.current.temperature - 32) / 1.8
    await client.close()
    await bot.send_message(message.from_user.id,
                           f'Current temperature in Bishkek is {round(current_t, 1)} °C')


async def jfk_sender(message: types.Message):
    client = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await client.find("New York")
    current_t = (weather.current.temperature - 32) / 1.8
    await client.close()
    await bot.send_message(message.from_user.id,
                           f'Current temperature in New York is {round(current_t, 1)} °C')


async def ber_sender(message: types.Message):
    client = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await client.find("Berlin")
    current_t = (weather.current.temperature - 32) / 1.8
    await client.close()
    await bot.send_message(message.from_user.id,
                           f'Current temperature in Berlin is {round(current_t, 1)} °C')


async def chi_sender(message: types.Message):
    client = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await client.find("Chicago")
    current_t = (weather.current.temperature - 32) / 1.8
    await client.close()
    await bot.send_message(message.from_user.id,
                           f'Current temperature in Chicago is {round(current_t, 1)} °C')


# @dp.message_handler(commands=['mem'])
async def mem_sender(message: types.Message):
    list_of_mem = os.listdir('media')
    chosen_mem = random.choice(list_of_mem)
    mem = open(f"media/{chosen_mem}", "rb")
    await bot.send_photo(message.from_user.id, photo=mem)


# @dp.message_handler(commands=['quiz'])
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


async def menu_sender(message: types.Message):
    # await bot.send_photo(message.from_user.id, test['photo'],
    #                            caption=f'Type: {test["type_of_dish"]}\n'
    #                            f'Name: {test["name"]}\n'
    #                            f'Description: {test["description"]}\n'
    #                            f'Price: {test["price"]}')
    pass


async def show_random_dish(message: types.Message):
    await select_dish_random_sql(message)






def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(mem_sender, commands=['mem'])
    dp.register_message_handler(quiz_handler, commands=['quiz'])
    dp.register_message_handler(weather_handler, commands=['weather'])
    dp.register_message_handler(fru_sender, commands=['Bishkek'])
    dp.register_message_handler(ber_sender, commands=['Berlin'])
    dp.register_message_handler(jfk_sender, commands=['New York'])
    dp.register_message_handler(chi_sender, commands=['Chicago'])
    dp.register_message_handler(currencies_handler, commands=['currencies'])
    dp.register_message_handler(eur_handler, commands=['EUR'])
    dp.register_message_handler(usd_handler, commands=['USD'])
    dp.register_message_handler(menu_sender, commands=['send_menu'])
    dp.register_message_handler(show_random_dish, commands=['random_dish'])
