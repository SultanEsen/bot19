import random
import sqlite3
from config import bot


def create_connection():
    global db, cursor
    try:
        db = sqlite3.connect('bot.sqlite3')
        cursor = db.cursor()
    except sqlite3.Error as e:
        print(e)

    if db:
        print('DB connected')
    try:
        db.execute(
                '''
                CREATE TABLE IF NOT EXISTS menu (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                photo TEXT,
                type VARCHAR(20) NOT NULL,
                name VARCHAR(100) NOT NULL,
                description VARCHAR(200) NOT NULL,
                price INTEGER NOT NULL DEFAULT 0
                )'''
            )
        db.commit()
    except sqlite3.Error as e:
        print(e)


async def insert_dish_sql(state):
    async with state.proxy() as data:
        print(data)
        cursor.execute('INSERT INTO menu (photo, type, name, description, price)'
                       'VALUES (?, ?, ?, ?, ?)', tuple(data.values()))
        db.commit()
        print(tuple(data.values()))
        print(f'New item added')


async def select_dish_random_sql(message):
    result = cursor.execute('SELECT * FROM menu').fetchall()
    temp_tuple = list(result)
    random_dish = random.choice(result)
    # print(result)
    print(random_dish)
    await bot.send_photo(message.from_user.id, random_dish[1],
                         caption=f'Type: {random_dish[2]}\n'
                                 f'Name: {random_dish[3]}\n'
                                 f'Description: {random_dish[4]}\n'
                                 f'Price: {random_dish[5]}')


async def select_all_dish_sql():
    return cursor.execute('SELECT * FROM menu').fetchall()


async def delete_dish_sql(id):
    cursor.execute('DELETE FROM menu WHERE id == ?', (id,))
    db.commit()

#
# async def select_by_composition(message):
#     result = cursor.execute('SELECT * FROM menu WHERE description LIKE "%Meat%"')
#     await bot.send_message(message.from_user.id, f'Hey')

