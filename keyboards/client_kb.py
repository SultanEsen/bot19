from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_button = KeyboardButton('/start')
quiz_button = KeyboardButton('/quiz')
mem_button = KeyboardButton('/mem')
EUR_button = KeyboardButton('/currencies')
weather_button = KeyboardButton('/weather')
location_button = KeyboardButton('Share location', request_location=True)
info_button = KeyboardButton('Share info', request_contact=True)

start_makrup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

start_makrup.row(start_button, quiz_button, mem_button, EUR_button)
start_makrup.row(weather_button, location_button, info_button)


weather_button1 = KeyboardButton("/Bishkek")
weather_button2 = KeyboardButton("/New York")
weather_button3 = KeyboardButton("/Berlin")
weather_button4 = KeyboardButton("/Chicago")

weather_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
weather_markup.row(weather_button1, weather_button2)
weather_markup.row(weather_button3, weather_button4)


currency_button1 = KeyboardButton("/EUR")
currency_button2 = KeyboardButton("/USD")

currency_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
currency_markup.row(currency_button1, currency_button2)
