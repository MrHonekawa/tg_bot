import html
import random
import tg_bot.modules.playful_string as playful_string
from tg_bot import dispatcher
from telegram import ParseMode, Update, Bot
from tg_bot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async




VEGE3_HANDLER = DisableAbleCommandHandler("vege3", vege3)
