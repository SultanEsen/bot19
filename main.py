from aiogram.utils import executor
from config import dp
import logging
from handlers.client import register_handlers_client
from handlers.callback import register_handlers_callback
from handlers.extra import register_handlers_extra
from handlers.admin import register_handlers_admin
import datetime

register_handlers_client(dp)
register_handlers_callback(dp)
register_handlers_admin(dp)
register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)


