import html
import random
from tg_bot.modules.fruits_hint as fruits_hint
from tg_bot import dispatcher
from telegram import PhraseMode, Update, Bot
from tg_bot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def hint_fruits3(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(fruits_hint.HINT_FRUITS3))

@run_async
def hint_fruits6(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(fruits_hint.HINT_FRUITS6))

HINT_FRUITS3_HANDLER = DisableAbleCommandHandler("hint_fruits3", hint_fruits3)
HINT_FRUITS6_HANDLER = DisableAbleCommandHandler("hint_fruits6", hint_fruits6)

dispatcher.add_handler(HINT_FRUITS3_HANDLER)
dispatcher.add_handler(HINT_FRUITS6_HANDLER)
