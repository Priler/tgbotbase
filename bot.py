from aiogram import executor
from dispatcher import dp
import handlers

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)