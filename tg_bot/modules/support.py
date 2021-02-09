import random, re
from random import randint
from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SUPPORT = (
       "Hello, Thanks for opting me up, This is my support group - @DragonAssociationSupport",
       "Hello, Thanks for opting me up, This is my support group - @DragonAssociationSupport",
)

UPDATE = (
      "Hello, Thanks for choosing us, This is my Update Channels @DragonUpdates & @TGBOTLAB",
      "Hello, Thanks for choosing us, This is my Update Channels @DragonUpdates & @TGBOTLAB",
)

SERVER = (
      "Hello, We holds a private server known as Dragonite Server have support here is a link to pvt server - https://discord.gg/crGUAnmSFD",
      "Hello, We holds a private server known as Dragonite Server have support here is a link to pvt server - https://discord.gg/crGUAnmSFD",
)

@run_async
def support_group(bot: Bot, update: Update):
  update.effective_message.reply_text(random.choice(SUPPORT))

@run_async
def update_channel(bot: Bot, update: Update):
  update.effective_message.reply_text(random.choice(UPDATE))

@run_async
def server(bot: Bot, update: Update):
  update.effective_message.reply_text(random.choice(SERVER))

SUPPORT_GROUP_HANDLER = DisableAbleCommandHandler("support_group", support_group)
UPDATE_CHANNEL_HANDLER = DisableAbleCommandHandler("update_channel", update_channel)
SERVER_HANDLER = DisableAbleCommandHandler("server", server)

dispatcher.add_handler(SUPPORT_GROUP_HANDLER)
dispatcher.add_handler(UPDATE_CHANNEL_HANDLER)
dispatcher.add_handler(SERVER_HANDLER)
