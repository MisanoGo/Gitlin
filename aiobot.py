from aiogram import Bot, Dispatcher


import apps

 
bot_token = "5996837717:AAEvTxi4RnvcL5rVx4pqdBcYByyQZhyjSXE"


async def fire():
    dp = Dispatcher()
    dp.include_router(apps.main_route)

    bot = Bot(token=bot_token, parse_mode="HTML")

    await dp.start_polling(bot)


