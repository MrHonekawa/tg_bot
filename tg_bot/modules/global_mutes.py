# Estella (A Telegram bot project)
# Copyright (C) Dragon Association & Estella Team
# Bot Running under Python3
# Yet to code.

import html
from io import BytesIO
from typing import Optional, List

from telegram import Message, Update, Bot, User, Chat
from telegram.error import BadRequest, TelegramError
from telegram.ext import run_async, CommandHandler, MessageHandler, Filters
from telegram.utils.helpers import mention_html

import tg_bot.modules.sql.global_mutes_sql as sql
from tg_bot import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, STRICT_GMUTE
from tg_bot.modules.helper_funcs.chat_status import user_admin, is_user_admin
from tg_bot.modules.helper_funcs.extraction import extract_user, extract_user_and_text
from tg_bot.modules.helper_funcs.filters import CustomFilters
from tg_bot.modules.helper_funcs.misc import send_to_list
from tg_bot.modules.sql.users_sql import get_all_chats

GMUTE_ENFORE_GROUP = 6


@run_async
def gmute(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    
    user_id, reason = extract_user_and_text(message, args)
    
    if not user_id:
      message.reply_text("You don't seem to referring a user.")
      return
    
    if int(user_id) in SUDO_USERS:
      message.reply_text("I spy, with my little eye... a sudo user war! Why you all are fighting with each other?")
      return
    
    if int(user_id) in SUPPORT_USERS:
      message.reply_text("OOHH someone is trying to gmute a sudo user! *grabs popcorn*")
      return
    
    if int(user_id) == bot.id:
      message.reply_text("-_- So funny, lets myself why don't I? Nice Try.")
      return
    
    try:
      user_chat = bot.get_chat(user_id)
    except BadRequest as excp:
      message.reply_text(excp.message)
      return
    
    if user_chat.type != 'private':
      message.reply_text("That's not a user!")
      return
    
    if sql.is_user_gmuted(user_id):
      if not reason:
        message.reply_text("This user is already gmuted; I'd change the reason, but you haven't given me one...")
        return
      
      sucess = sql.update_gmute_reason(user_id, user_chat.username or user_chat.first_name, reason)
      if sucess:
            message.reply_text("This user is already gmuted; I've gone and updated the gmute reason tough!")
      else:
          message.reply_text("Huh, do you mind trying that again? I thought this person was gmuted, but she/he wasn't? "
                             "I am very confused")
            
      return

message.reply_text("Getting the ducts ready oppose your gmute in @DragonAssociationSupport")

muter = update.effective_user
send_to_list(bot, SUDO_USERS + SUPPORT_USERS,
             "{} is gmuting user {} "
             "because:\n{}".format(mention_html(muter.id, muter.first_name),
                                   mention_html(user_chat.id, user_chat.first_name), reason or "No Reason Given"),
             html=True)

sql.gmute_user(user_id, user_chat.username or user_chat.first_name, reason)

