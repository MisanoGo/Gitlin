from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

import apps
import utils


PROXY = utils.env_conf["PROXY"]
BOT_TOKEN = utils.env_conf["BOT_TOKEN"]

bot = Bot(BOT_TOKEN,AiohttpSession(PROXY),"HTML")


async def fire(bot: Bot, BOT_TOKEN: str):
    # set telegram bot initialiser
    dp = Dispatcher()
    dp.include_router(apps.main_route)

    await dp.start_polling(bot)

