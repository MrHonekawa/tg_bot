import html
import random
import tg_bot.modules.playful_string as playful_string
from tg_bot import dispatcher
from telegram import ParseMode, Update, Bot
from tg_bot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@runs_async
def fruits3(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(playful_string.FRUITS3))

@run_async
def fruits6(update: Update, context: CallbackContext):
  args = context.args
  update.effective_messafe.reply_text(random.choice(playful_string.FRUITS6))

FRUITS3_HANDLER = DisableAbleCommandHandler("fruits3", fruits3)
FRUITS6_HANDLER = DisableAbleCommandHandler("fruits6", fruits6)

dispatcher.add_handler(FRUITS3_HANDLER)
dispatcher.add_handler(FRUITS6_HANDLER)
