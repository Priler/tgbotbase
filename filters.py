from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
import config

class IsOwnerFilter(BoundFilter):
    """
    Custom filter "is_owner".
    """
    key = "is_owner"

    def __init__(self, is_owner):
        self.is_owner = is_owner
    
    async def check(self, message: types.Message):
        return message.from_user.id == config.BOT_OWNER