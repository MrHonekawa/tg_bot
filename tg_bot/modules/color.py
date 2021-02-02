import random, re
from random import randint
from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

COLOR4 = ( 
     "Red"
     "White",
     "Green",
     "Yellow",
     "Peach",
     "Voilet",
     "Pink",
     "Purple"
)

COLOR6 = (
      "Blue"
      "Black",
      "Golden",
      "Silver",
      "Indigo",
      "Orange",
      "Brown"
      "Red",
      "Green",
      "Yellow",
      "Peach",
      "Purple"

)

HINT_COLOR4 = (
           "Color Guessing games played between 4 players. Guess color by getting hint -- 1) Red, 2) White, 3) Green, 4) Yellow, 5) Peach, 6) Voilet, 7) Pink, 8) Purple"

)

HINT_COLOR6 = (
           "Color Guessing games played between 6 players. Guess color by getting hint -- 1) Blue, 2) Black, 3) Golden, 4) Silver, 5) Indigo, 6) Orange, 7) Brown, 8) Red, 9) Green, 10) Yellow, 11) Peach, 12) Purple"

)

@run_async
def color4(bot: Bot, update: Update):
  update.message.reply_text(random.choice(COLOR4))

@run_async
def color6(bot: Bot, update: Update):
  update.message.reply_text(random.choice(COLOR6))

@run_async
def hint_color4(bot: Bot, update: Update):
     update.message.reply_text(random.choice(HINT_COLOR4))

@run_async
def hint_color6(bot: Bot, update: Update):
     update.message.reply_text(random.choice(HINT_COLOR6))

__help__ = """
- /color4 : Color Guessing game played between 4 players. Type /hint_color4 for hint. (Hint Allowed)
"""
