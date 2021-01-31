import html
import random
import tg_bot.modules.server_string as server_string
from tg_bot import dispatcher
from telegram import ParseMode, Update, Bot
from tg_bot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def server(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(server_string.SERVER))
    
    SERVER_HANDLER = DisableAbleCommandHandler("server", server)
    
    dispatcher.add_handler(SERVER_HANDLER)
