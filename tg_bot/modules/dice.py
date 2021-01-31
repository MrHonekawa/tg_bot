import html
import random
import tg_bot.modules.dice_string as dice_string
from tg_bot import dispatcher
from telegram import ParseMode, Update, Bot
from tg_bot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def dice6(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(dice_string.DICE6))

@run_async
def dice12(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(dice_string.DICE12))
                                      
@run_async
def dice18(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(dice_string.DICE18))

@run_async
def dice4(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(dice_string.DICE4))

@run_async
def dice2(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(dice_string.DICE2))

DICE6_HANDLER = DisableAbleCommandHandler("dice6", dice6)
DICE12_HANDLER = DisableAbleCommandHandler("dice12", dice12)
DICE18_HANDLER = DisableAbleCommandHandler("dice18", dice18)
DICE4_HANDLER = DisableAbleCommandHandler("dice4", dice4)
DICE2_HANDLER = DisableAbleCommandHandler("dice2", dice2)

__help__ = """
Hello, welcome to Games Section.
You can play aswme games anytime...
List of GAMES-
- DICE
-- /dice2 : rolls the dice with measuring 1-2 numbers as main.
-- /dice4 : rolls the dice with measuring 1-4 numbers as main.
-- /dice6 : rolls the dice with measuring 1-6 numbers as main.
-- /dice12 : rolls the dice with measuring 1-12 numbers as main.
-- /dice18 : rolls the dice with measuring 1-18 numbers as main.

- VEGETABLES
-- /vege3 : play vegetables game with 3 friends only.... not more then that! 
To get hint type /hint_vege3
-- /vege6 : play vegetables game with 6 friends only not more then that!
To get hint type /hint_vege6

- COLOUR 
-- /color4 : play colour game with 4 friends only.... not more then that!
To get hint type /hint_color4
-- /color6 : play colour game with 6 friends only.... not more then that!
To get hint type /hint_color6


"""
__mod_name__ = "GAMES"
