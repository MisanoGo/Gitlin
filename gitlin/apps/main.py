from aiogram import Bot
from aiogram.methods import SendMessage
from aiogram.filters import Command
from aiogram.types import Message

from apps import main_route
from gitlin.db import repo


@main_route.startup()
async def startup(bot: Bot):
    message: str = "hi, im there."
    for chat_id in repo.groupList:
        bot.send_message(chat_id,message)

@main_route.message(Command('start'))
def start_cmd(message: Message):
    msg: str = ""
    return message.answer(msg)

@main_route.message(Command('help'))
def help_cmd(message: Message):
    msg: str = ""
    return message.answer(msg)

@main_route.message(Command('license'))
def licence_cmd(message: Message):
    msg: str = open("LICENSE","r").read()
    return message.answer(msg)
