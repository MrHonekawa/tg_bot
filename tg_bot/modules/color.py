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

@run_async
def color4(bot: Bot, update: Update):
  update.message.reply_text(random.choice(COLOR4))

@run_async
def color6(bot: Bot, update: Update):
  update.message.reply_text(random.choice(COLOR6))
