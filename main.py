from aiogram.utils import executor
from decouple import config

from config import dp, URL, bot, PORT
import logging
from handlers.notification import register_handlers_notifications, scheduler
from handlers.client import register_handlers_client
from handlers.callback import register_handlers_callback
from handlers.extra import register_handlers_extra
from handlers.admin import register_handlers_admin
from handlers.fsm_menu import register_handlers_fsm_menu
from handlers.inline import register_inline_handler
# import datetime
from database.bot_db import create_connection
import asyncio


async def on_startup(_):
    await bot.set_webhook(URL)
    asyncio.create_task(scheduler())
    create_connection()


async def on_shutdown(dp):
    await bot.delete_webhook()


register_handlers_notifications(dp)
register_handlers_client(dp)
register_handlers_callback(dp)
register_handlers_admin(dp)
register_handlers_fsm_menu(dp)
register_inline_handler(dp)
register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path='',
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host='0.0.0.0',
        port=config('PORT', cast=int),

    )