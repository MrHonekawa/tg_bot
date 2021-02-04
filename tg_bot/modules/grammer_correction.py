# Estella (A Telegram bot project)
# Copyright (C) Dragon Association & Estella Team
# Code not done yet.

import json
from pprint import pprint

import requests
from telegram import Update, Bot
from telegram.ext import CommandHandler

from tg_bot import dispatcher

# Open API_KEY
API_KEY = "6ae0c3a0-afdc-4532-a810-82ded0054236"
URL = "http://services.gingersoftware.com/Ginger/correct/json/GingerTheText"


def grammer(bot: Bot, update: Update):
  if update.effective_message.reply_to_message:
    msg = update.effective_message.reply_to_message

# Still Left to code.
