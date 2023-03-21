from enum import Enum

from aiogram.filters import Command
from aiogram.fsm import State, FSMContext, StateGroup
from aiogram.utils import InlineKeyboardMarkup
from aiogram.types import Message, CallbackData

from gitlin.filters import f_ftc, f_is_rgs
from gitlin.db import repo

from apps import main_route


#class SetupForm(StateGroup):

#    chose_topic = State()

class ServicesActions(str, Enum):
    notification = "notification"
    # the other services

class TopicCreatorAction(CallbackData):
    action: ServicesActions
    chat_id: int
    user_id: int
    topic_id : int

@main_route.message(Command("register"))
async def register(message: Message):
    pass

@main_route.message(f_ftc,f_is_rgs)
async def topic_created(message: Message):
    b = InlineKeyboardMarkup()
    for action in ServicesActions:
        b.button(
            action.value.title(),
            callback_data=TopicCreatorAction(
                                             action=action,
                                             chat_id=message.chat.id,
                                             user_id=message.from_user.id,
                                             topic_id=message.message_thread_id))
    await message.answer("hi\nlets define services witch you like to enable it",reply_markup=b)

@main_route.callback_query(TopicCreatorAction)
async def a():
    pass
