import html
import random
import tg_bot.modules.support_group as support_group
from tg_bot import dispatcher
from telegram import ParseMode, Update, Bot
from tg_bot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def support_group(update: Update, context: CallbackContext):
