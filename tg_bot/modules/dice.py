import random, re
from random import randint
from telegram import Message, Update, Bot, Users
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

DICE2 = (
     "1",
     "2",
     "3",
)

DICE3 = (
     "1",
     "2",
     "3",
     "4",
)

DICE4 = (
     "1",
     "2",
     "3",
     "4",
     "5",
)

DICE5 = (
     "1",
     "2",
     "3",
     "4",
     "5",
     "6",
)

DICE6 = (
     "1",
     "2",
     "3",
     "4",
     "5",
     "6",
     "7",
)

@run_async
def dice2(bot: Bot, update: Update):
  update.message.reply_text(random.choice(DICE2))

@run_async
def dice3(bot: Bot, update: Update):
  update.message.reply_text(random.choice(DICE3))

@run_async
def dice4(bot: Bot, update: Update):
  update.message.reply_text(random.choice(DICE4))

@run_async
def dice5(bot: Bot, update: Update):
  update.message.reply_text(random.choice(DICE5))

@run_async
def dice6(bot: Bot, update: Update):
  update.message.reply_text(random.choice(DICE6))

__help__ = """
- /dice2 : rolls a dice when there is 2 players.
- /dice3 : rolls a dice when there is 3 players.
- /dice4 : rolls a dice when there is 4 players.
- /dice5 : rolls a dice when there is 5 players.
- /dice6 : rolls a dice when there is 6 players.
"""

__mod_name__ = "Dice Game"

DICE2_HANDLER = DisableAbleCommandHandler("dice2", dice2)
DICE3_HANDLER = DisableAbleCommandHandler("dice3", dice3)
DICE4_HANDLER = DisableAbleCommandHandler("dice4", dice4)
DICE5_HANDLER = DisableAbleCommandHandler("dice5", dice5)
DICE6_HANDLER = DisableAbleCommandHandler("dice6", dice6)

dispatcher.add_handler(DICE2_HANDLER)
dispatcher.add_handler(DICE3_HANDLER)
dispatcher.add_handler(DICE4_HANDLER)
dispatcher.add_handler(DICE5_HANDLER)
dispatcher.add_handler(DICE6_HANDLER)
