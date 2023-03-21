from aiogram import F

from db import repo


f_ftc = F.forum_topic_created != None
f_is_rgs = F.chat_id in repo.groupList()
