import html
import random
import tg_bot.modules.vege_hint as vege_hint
from tg_bot import dispatcher
from telegram import ParseMode, Update, Bot
from tg_bot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def hint_vege3(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(vege.HINT_VEGE3))
  
@run_async
def hint_vege6(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(vege.HINT_VEGE6))


HINT_VEGE3_HANDLER = DisableAbleCommandHandler("hint_vege3", hint_vege3)
HINT_VEGE6_HANDLER = DisableAbleCommandHandler("hint_vege6", hint_vege6)

dispatcher.add_handler(HINT_VEGE3_HANDLER)
dispatcher.add_handler(HINT_VEGE6_HANDLER)
