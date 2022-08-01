from aiogram import types, Dispatcher
from config import ADMIN


async def kick(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMIN:
            await message.answer(f'You are not an admin')
        elif not message.reply_to_message:
            await message.answer(f'Specify a message of user you want to kick')
        else:
            await message.bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.answer(f'User {message.reply_to_message.from_user.full_name} was kicked')
    else:
        await message.answer(f'It works only in group chat')


async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMIN:
            await message.answer(f'You are not an admin')
        elif not message.reply_to_message:
            await message.answer(f'Specify a message of user you want to ban')
        else:
            await message.bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.answer(f'User {message.reply_to_message.from_user.full_name} was banned for some time')
    else:
        await message.answer(f'It works only in group chat')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(kick, commands=['kick'], commands_prefix='/!')
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='/!')
