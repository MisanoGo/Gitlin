from aiogram import Bot, Dispatcher

import apps

async def fire(BOT_TOKEN: str):
    # set telegram bot initialiser
    dp = Dispatcher()
    dp.include_router(apps.main_route)

    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    await dp.start_polling(bot)

