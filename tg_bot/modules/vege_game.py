import html
import random
import tg_bot.modules.playful_string as playful_string
from tg_bot import dispatcher
from telegram import ParseMode, Update, Bot
from tg_bot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def vege3(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(playful_string.VEGE3))
  
@run_async
def vege6(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(playful_string.VEGE6))

