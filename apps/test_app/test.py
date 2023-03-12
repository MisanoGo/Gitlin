from aiogram import Router, types
from aiogram.filters import Command

tst_rt: Router = Route('test_route')

@tst_rt.message(Command(command=["start"]))
async def test(message: types.Message):
    await message.answer('this is test')

