from aiogram.utils import executor
from config import dp
import logging
from handlers.notification import register_handlers_notifications, scheduler
from handlers.client import register_handlers_client
from handlers.callback import register_handlers_callback
from handlers.extra import register_handlers_extra
from handlers.admin import register_handlers_admin
from handlers.fsm_menu import register_handlers_fsm_menu
import datetime
from database.bot_db import create_connection
import asyncio


async def on_startup(_):
    asyncio.create_task(scheduler())
    create_connection()


register_handlers_notifications(dp)
register_handlers_client(dp)
register_handlers_callback(dp)
register_handlers_admin(dp)
register_handlers_fsm_menu(dp)
register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
