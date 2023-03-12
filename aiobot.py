from aiogram import Bot, Dispatcher


import apps

bot_token = ""

async def main():
    dp = Dispatcher()
    dp.include_router(apps.app_routers)

    bot = Bot(token=bot_token, parse_mode="HTML")

    await dp.start_polling(bot)


