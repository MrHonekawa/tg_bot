# Estella (A Telegram bot project)
# Copyright (C) Dragon Association & Estella Team
# Copyright (C) 2021
# AI Module by Estella Team
from time import time, sleep

from coffehouse.lydia import LydiaAI
from coffehouse.api import API
from coffehouse.exception import CoffeHouseError as CFError

from telegram import Message, Chat, User, Update, Bot
from telegram.ext import CommandHandler, MessageHandler, Filters, run_async
from telegram.error import BadRequest, Unauthorized, RetryAfter

from tg_bot import dispatcher, API_KEY, OWNER_ID
import tg_bot.modules.sql.chatbot_sql as sql
from tg_bot.modules.helper_funcs.filters import CustomFilters

CoffeHouseAPI = API(API_KEY)
api_client = LydiaAI(CoffeHouseAPI)

@run_async
def startchatbot(bot: Bot, update: Update):
  global api_client
  chat_id = update.effective_chat.id
  msg = update.effective_message
  is_chat = sql.is_chat(chat_id)
  if not is_chat:
    ses = api_client.create_session()
    ses_id = str(ses.id)
    expires = str(ses.expires)
    sql.set_ses(chat_id, ses_id, expires)
    msg.reply_text("Enabled AI chatbot Estella in this group")
  else:
    msg.reply_text("Estella AI chatbot is already enabled in this group")
    
@run_async
def stopchatbot(bot: Bot, update: Update):
  msg = update.effective_message
  chat_id = update.effective_chat.id
  is_chat = sql.is_char(chat_id)
  if not is_chat:
    msg.reply_text("Estella AI chatbot is not enabled in this group")
  else:
    sql.rem_chat(chat_id)
    msg.reply_text("Estella AI chatbot is disabled in this group")
 

@run_asyc
def check_message(bot: Bot, message):
  reply_msg = message.reply_to_message
  if message.text.lower() == "estella":
    return True
  if reply_msg:
    if reply_msg.from_user.id == bot.get_me().id:
      return True
    else:
      return False
    
    
@run_async
def chatbot(### Yet to code from here ###
