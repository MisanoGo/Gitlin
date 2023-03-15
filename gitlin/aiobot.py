from aiogram import Bot, Dispatcher

import apps
import utils


BOT_TOKEN = utils.env_conf["BOT_TOKEN"]
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")

async def fire(bot: Bot, BOT_TOKEN: str):
    # set telegram bot initialiser
    dp = Dispatcher()
    dp.include_router(apps.main_route)

    await dp.start_polling(bot)

