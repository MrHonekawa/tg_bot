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
  update.effective_message.reply_text(random.choice(dice_string.DICE6)

@run_async
def dice12(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(dice_string.DICE12)
                                      
@run_async
def dice18(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(dice_string.DICE18)
                                      
DICE6_HANDLER = DisableAbleCommandHandler("dice6", dice6)
DICE12_HANDLER = DisableAbleCommandHandler("dice12", dice12)
DICE18_HANDLER = DisableAbleCommandHandler("dice18", dice18)
