import random, re
from random import randint
from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

CAR2 = (
  "Ford Raptor",
  "Lamborgini Diablo",
  "Ferrari Testarossa",
)

CAR3 = (
  "Porsche 911",
  "Ferrari 812",
  "Lamborgini Diablo",
  "Ford Raptor",
)

HINT_CAR2 = (
  "Car name guessing game played between 2 players. Hint are - 1) Ford Raptor 2) Lamborgini Diablo 3) Ferrari Testarossa",
  "Car name guessing game played between 2 players. Hint are - 1) Ford Raptor 2) Lamborgini Diablo 3) Ferrari Testarossa",
)

HINT_CAR3 = (
  "Car name guessing game played between 3 players. Hints are not available yet hope comes in next update",
  "Car name guessing game played between 3 players. Hints are not available yet hope comes in next update",
)

@run_async
def car2(bot: Bot, update: Update):
  update.message.reply_text(random.choice(CAR2))

@run_async
def car3(bot: Bot, update: Update):
  update.message.reply_text(random.choice(CAR3))

@run_async
def hint_car2(bot: Bot, update: Update):
  update.message.reply_text(random.choice(HINT_CAR2))

@run_async
def hint_car3(bot: Bot, update: Update):
  update.message.reply_text(random.choice(HINT_CAR3))

__help__ """
Here is CAR GAME MODULE :-
- /car2 : Car Name Guessing game played between 2 players.
- /hint(_)car2 : Get hint on playing game (Remove Brackets in CMD)
- /car3 : Car Name Guessing game played between 3 players.
- /hint(_)car3 : Get hint on playing game (Remove Brackets in CMD)
"""

__mod_name__ = "CAR GAME"

CAR2_HANDLER = DisableAbleCommandHandler("car2", car2)
CAR3_HANDLER = DisableAbleCommandHandler("car3", car3)
HINT_CAR2_HANDLER = DisableAbleCommandHandler("hint_car2", hint_car2)
HINT_CAR3_HANDLER = DisableAbleCommandHandler("hint_car3", hint_car3)

dispatcher.add_handler(CAR2_HANDLER)
dispatcher.add_handler(CAR3_HANDLER)
dispatcher.add_handler(HINT_CAR2_HANDLER)
dispatcher.add_handler(HINT_CAR3_HANDLER)
