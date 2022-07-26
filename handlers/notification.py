import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    print('ok')
    await bot.send_message(chat_id=chat_id, text='Ok!')


async def classes():
    await bot.send_message(chat_id=chat_id, text='Today at 18:00 there will be programming classes')


async def scheduler():
    aioschedule.every().tuesday.at("09:00").do(classes)
    aioschedule.every().friday.at("09:00").do(classes)


    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notifications(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: "classes" in word.text)



