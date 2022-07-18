import random
import time
import asyncio
from aiogram import types, Dispatcher
from config import bot
from config import ADMIN


# @dp.message_handler()
async def echo(message: types.Message):
    # try:
    #     current_message = int(message.text)
    #     await bot.send_message(message.from_user.id, current_message ** 2)
    # except:
    #     await bot.send_message(message.from_user.id, message.text)
    bad_words = ['bitch', 'fuck', 'shit', 'bint',]
    for word in bad_words:
        if word in message.text.replace(" ", "").lower():
            temp_mess = await bot.send_message(message.chat.id, f'Wow, {message.from_user.full_name}, calm down!\n'
                                f'Please be more tolerant, it is public chat!')
            await bot.delete_message(message.chat.id, message.message_id)
            time.sleep(5)
            await bot.delete_message(message.chat.id, temp_mess.message_id)
            print(f'Your message #{temp_mess.message_id} is deleted')
            break

    if message.text.startswith('!pin'):
        if not message.reply_to_message:
            await bot.send_message(message.chat.id, f'Specify a message to pin (reply to that)')
        else:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)

    if message.text.lower() == 'dice':
        a = await bot.send_dice(message.chat.id, emoji='🎲')
        await bot.send_message(message.chat.id, f'Your throw')
        b = a.dice.value
        print(b)
        c = await bot.send_dice(message.chat.id, emoji='🎲')
        await bot.send_message(message.chat.id, f'My throw')
        d = c.dice.value
        print(d)
        await asyncio.sleep(5)
        if b > d:
            await bot.send_message(message.chat.id, f'You won')
        elif b < d:
            await bot.send_message(message.chat.id, f'I won')
        else:
            await bot.send_message(message.chat.id, f'Leg and leg')


    if message.text.startswith('game'):
        if message.from_user.id not in ADMIN:
            await bot.send_message(message.chat.id, f'The game is available only for admins')
        else:
            list_of_emoji = ['🎲', '⚽', '🏀', '🎯', '🎰', '🎳']
            emoji = random.choice(list_of_emoji)
            await bot.send_dice(message.chat.id, emoji=emoji)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)