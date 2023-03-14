from aiogram import Router, types
from aiogram.filters import Command

tst_rt: Router = Router()

@tst_rt.message(Command("start"))
async def test(message: types.Message):
    await message.answer('this is test')

