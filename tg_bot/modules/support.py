import random, re
from telegram import randint
from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SUPPORT = (
       "Hello, Thanks for opting me up, This is my support group - @DragonAssociationSupport"
)

UPDATE = (
      "Hello, Thanks for choosing us, This is my Update Channels @DragonUpdates & @TGBOTLAB"
)

@run_async
def support_group(bot: Bot, update: Update):
  update.effective_message.reply_text(random.choice(SUPPORT))

@run_async
def update_channel(bot: Bot, update; Update):
  update.effective_message.reply_text(random.choice(UPDATE))

SUPPORT_GROUP_HANDLER = DisableAbleCommandHandler("support_group", support_group)
UPDATE_CHANNEL_HANDLER = DisableAbleCommandHandler("update_channel", update_channel)

dispatcher.add_handler(SUPPORT_GROUP_HANDLER)
dispatcher.add_handler(UPDATE_CHANNEL_HANDLER)
