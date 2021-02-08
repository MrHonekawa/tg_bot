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

CoffeHouseAPI = API(AI_API_KEY)
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
def chatbot(bot: Bot, update: Update):
  global api_client
  msg = update.effective_message
  chat_id = update.effective_chat.id
  is_chat = sql.is_chat(chat_id)
  if not is_chat:
    return
  if msg.text and not msg.document:
    if not check_message(bot, msg):
      return
    sesh, exp = sql.get_ses(chat_id)
    query = msg.text
    try:
      if int(exp) < time():
        ses = api_client.create_session()
        ses_id = str(ses.id)
        expires = str(ses.expires)
        sql.set_ses(chat_id, ses_id, expires)
        sesh, exp = sql.get_ses(chat_id)
    except ValueError:
      pass
    try:
      bot.send_chat_action(chat_id, action='typing')
      rep = api_client.think_thought(sesh, query)
      sleep(0.6)
      msg.reply_text(rep, timeout=60)
    except CFError as e:
      bot.send_message(OWNER_ID, f"Chatbot Error: {e} occurred in {chat_id}!")
      
      
@run_async
def list_chatbot_chats(bot: Bot, update: Update):
    chats = sql.get_all_chats()
    text = "<b>ESTELLA AI-Enabled Chats</b>\n"
    for chat in chats:
        try:
            x = bot.get_chat(int(*chat))
            name = x.title if x.title else x.first_name
            text += f"• <code>{name}</code>\n"
        except BadRequest:
            sql.rem_chat(*chat)
        except Unauthorized:
            sql.rem_chat(*chat)
        except RetryAfter as e:
            sleep(e.retry_after)
    update.effective_message.reply_text(text, parse_mode="HTML")
    
def __stats__():
  return "• Total Chats Enabled AI : {}".format(sql.get_all_chats())

__help__ = """
Here is help for CHATBOT MODULE
Go to @DragonAssociationSupport and ask them to enable chatbot in your group.
We also have chatbot enabled group where you can know how this works. @EstellaAI
"""

__mod_name__ = "CHATBOT"

STARTCHATBOT_HANDLER = CommandHandler("enable_ai", startchatbot, filters=CustomFilters.sudo_fiter)
STOPCHATBOT_HANDLER = CommandHandler ("disable_ai", stopchatbot, filters=CustomFilters.sudo_filter)
CHATBOT_HANDLER = MessageHandler(Filters.text & (~Filters.regex(r"^#[^\s]+") & ~Filters.regex(r"^!")
                                  & ~Filters.regex(r"^s\/")), chatbot)
LIST_CHATBOT_CHATS_HANDLER = CommandHandler("ai_chats", list_chatbot_chats, filters=CustomFilters.sudo_filter)

dispatcher.add_handler(STARTCHATBOT_HANDLER)
dispatcher.add_handler(STOPCHATBOT_HANDLER)
dispatcher.add_handler(CHATBOT_HANDLER)
dispatcher.add_handler(LIST_CHATBOT_CHATS_HANDLER)

# Code Completed
