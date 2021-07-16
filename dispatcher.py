from aiogram import Bot, Dispatcher
from filters import IsOwnerFilter
import config

# init
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# activate filters
dp.filters_factory.bind(IsOwnerFilter)