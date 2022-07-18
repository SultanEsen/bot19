from aiogram import types, Dispatcher
from config import bot
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton




# @dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

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


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("NEXT", callback_data='button_call_3')
    markup.add(button_call_3)

    question = "How many satellites does Mars hold?"
    answers = [
        "1",
        "2",
        "3",
        "4"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Think well",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    # button_call_4 = InlineKeyboardButton("NEXT", callback_data='button_call_4')
    # markup.add(button_call_4)

    question = "What is the area of the planet earth (in square km)?"
    answers = [
        "510 mln",
        "505 mln",
        "515 mln",
        "450 mln"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Think well",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")
    dp.register_callback_query_handler(quiz_4, lambda call: call.data == "button_call_3")
