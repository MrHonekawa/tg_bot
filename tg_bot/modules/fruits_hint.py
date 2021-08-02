import random, re
from random import randint
from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

FRUITS3 = (
       "Apple",
       "Banana",
       "Pineapple",
       "Watermelon",
       "Orange",
       "Grapes",
)

FRUITS6 = (
       "NOT AVALABILE"
)

HINT_FRUITS3 = (
            "Guessing Fruits Game played along 3 players. You have to guess fruits name by hints given below -- 1) Apple, 2) Banana, 3) Pineapple, 4) WaterMelon, 5) Orange, 6) Grapes"
)

HINT_FRUITS6 = (
            "Provided Soon, Hopefully in next update if you want this hint to be revealed faster req to @DragonAssociationSupport"
)

@run_async
def fruits3(bot: Bot, update: Update):
    update.message.reply_text(random.choice(FRUITS3))

@run_async
def fruits6(bot: Bot, update: Update):
    update.message.reply_text(random.choice(FRUITS6))

@run_async
def hint_fruits3(bot: Bot, update: Update):
    update.message.reply_text(random.choice(HINT_FRUITS3))

@run_async
def hint_fruits6(bot: Bot, update: Update):
    update.message.reply_text(random.choice(HINT_FRUITS6))

__help__ = """
- `/fruits3` : Guessing Fruits Game played along 3 players.
- `/hint_fruits3` : Get hint for playing game
- `/fruits6` : Guessing Fruits Game played along 6 players.
- `/hint_fruits6` : Get hint for playing game.
"""

__mod_name__ = "Fruits Game"

FRUITS3_HANDLER = DisableAbleCommandHandler("fruits3", fruits3)
FRUITS6_HANDLER = DisableAbleCommandHandler("fruits6", fruits6)
HINT_FRUITS3_HANDLER = DisableAbleCommandHandler("hint_fruits3", hint_fruits3)
HINT_FRUITS6_HANDLER = DisableAbleCommandHandler("hint_fruits6", hint_fruits6)

dispatcher.add_handler(FRUITS3_HANDLER)
dispatcher.add_handler(FRUITS6_HANDLER)
dispatcher.add_handler(HINT_FRUITS3_HANDLER)
dispatcher.add_handler(HINT_FRUITS6_HANDLER)
