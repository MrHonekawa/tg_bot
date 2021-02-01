import html
import random
import tg_bot.modules.support_group as support_group
from tg_bot import dispatcher
from telegram import ParseMode, Update, Bot
from tg_bot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def support_group(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice.SUPPORT))

@run_async
def update_channel(update: Update, context; CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice.UPDATE))

SUPPORT_GROUP_HANDLER = DisableAbleCommandHandler("support_group", support_group)
UPDATE_CHANNEL_HANDLER = DisableAbleCommandHandler("update_channel", update_channel)

dispatcher.add_handler(SUPPORT_GROUP_HANDLER)
dispatcher.add_handler(UPDATE_CHANNEL_HANDLER)
