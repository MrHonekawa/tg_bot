import html
import random
import tg_bot.modules.color_hint as color_hint
from tg_bot import dispatcher
from telegram import ParseMode, Update, Bot
from tg_bot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def color4(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(color_hint.COLOR4))

@run_async
def color6(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(color_hint.COLOR6))

COLOR4_HANDLER = DisableAbleCommandHandler("hint_color4", color4)
COLOR6_HANDLER = DisableAbleCommandHandler("hint_color6", color6)

dispatcher.add_handler(COLOR4_HANDLER)
dispatcher.add_handler(COLOR6_HANDLER)
