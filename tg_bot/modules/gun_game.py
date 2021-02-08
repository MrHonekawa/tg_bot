# Estella (A Telegram bot project)
# Copyright (C) Dragon Association & Estella Team
# Copyright (C) 2021
# Thanks to JosephFrank for this game module.

import random, re
from random import randint
from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

GUN_NAME = (
  "Rifles",
  "Carbines",
  "Machine Gun",
  "Sniper Rifle",
  "Automatic Rifle",
  "Assault Rifle",
  "SubMachine Guns",
)

@run_async
def gun_name(bot: Bot, update: Update):
  update.message.reply_text(random.choice(GUN_NAME))

__help__ = """
Here is GUN GAME Module
- /gun : Guess guns type name
- No hint available
- No guns are there like AK47, M416.
"""

__mod_name__ = "GUN GAME"

GUN_NAME_HANDLER = DisableAbleCommandHandler("gun", gun_name)

dispatcher.add_handler(GUN_NAME_HANDLER)
