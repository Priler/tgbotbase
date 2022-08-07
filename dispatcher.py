import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv
from filters import IsOwnerFilter, IsAdminFilter, MemberCanRestrictFilter
import os

# Find .env file
load_dotenv(find_dotenv())

# Configure logging
logging.basicConfig(level=logging.INFO)

# prerequisites
if not os.getenv('BOT_TOKEN'):
    exit("No token provided")

# init
bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode="HTML")
dp = Dispatcher(bot)

# activate filters
dp.filters_factory.bind(IsOwnerFilter)
dp.filters_factory.bind(IsAdminFilter)
dp.filters_factory.bind(MemberCanRestrictFilter)
