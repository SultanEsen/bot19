from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot
from config import ADMIN
from keyboards.client_kb import type_of_dish_markup, cancel_markup

class FSMAdmin(StatesGroup):
    photo = State()
    type_of_dish = State()
    name = State()
    description = State()
    price = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id in ADMIN:
            await FSMAdmin.photo.set()
            await message.answer(f'Hello, {message.from_user.full_name}! \n'
                                 f'Send me a photo of dish you wanna add to menu:', reply_markup=cancel_markup)
        else:
            await message.reply('Only for admins')
    else:
        await message.reply('Only in private chat')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # data['id'] = message.from_user.id
        # data['username'] = f'@{message.from_user.username}'
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer(f'Type type of dish:', reply_markup=type_of_dish_markup)


async def type_of_dish(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type_of_dish'] = message.text
    await FSMAdmin.next()
    await message.answer(f'Type a name of dish:', reply_markup=cancel_markup)


async def name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer(f'Type description of dish:')


async def description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer(f'Enter price of dish:')


async def price(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['price'] = int(message.text)
        print(data)
        await bot.send_photo(message.from_user.id, data['photo'],
                             caption=f'Type: {data["type_of_dish"]}\n'
                               f'Name: {data["name"]}\n'
                               f'Description: {data["description"]}\n'
                               f'Price: {data["price"]}')
        await state.finish()
        await message.answer("The new dish was added.")
    except:
        await message.answer('Enter digits')


async def cansel_adding(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer(f'Adding was stopped')


def register_handlers_fsm_menu(dp: Dispatcher):
    dp.register_message_handler(cansel_adding, state='*', commands=['cancel'])
    dp.register_message_handler(cansel_adding, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['menu'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(type_of_dish, state=FSMAdmin.type_of_dish)
    dp.register_message_handler(name, state=FSMAdmin.name)
    dp.register_message_handler(description, state=FSMAdmin.description)
    dp.register_message_handler(price, state=FSMAdmin.price)
