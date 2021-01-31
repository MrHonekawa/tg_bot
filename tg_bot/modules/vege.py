import html
import random
import tg_bot.modules.vege as vege
from tg_bot import dispatcher
from telegram import ParseMode, Update, Bot
from tg_bot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def vege3(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(vege.HINT_VEGE3))
  
@run_async
def vege6(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(vege.HINT_VEGE6))


VEGE3_HANDLER = DisableAbleCommandHandler("vege3", vege3)
VEGE6_HANDLER = DisableAbleCommandHandler("vege6", vege6)

dispatcher.add_handler(VEGE3_HANDLER)
dispatcher.add_handler(VEGE6_HANDLER)
