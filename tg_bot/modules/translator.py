import random
from typing import Optional, List

from telegram import Message, Update, Bot, ParseMode, Chat
from telegram.ext import run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.string_handling import remove emoji
from tg_bot.modules.tr_engine.strings import tld, tld_list

from googletrans import LANGUAGES, Translator

@run_async
def do_translate(bot: Bot, update: Update, args: List[str]):
    chat = update.effective_chat 
    msg = update.effective_message 

    if msg.reply_to_message:
        to_translate_text = remove_emoji(msg.reply_to_message.text)
    else:
        msg.reply_text(tld(chat.id, "translator_no_str"))
        return

    if not args:
        msg.reply_text(tld(chat.id, 'translator_no_args'))
        return
    lang = args[0]

    translator = Translator()
    try:
        translated = translator.translate(to_translate_text, dest=lang)
    except ValueError as e:
        msg.reply_text(tld(chat.id, 'translator_err').format(e))
        return

    src_lang = LANGUAGES[f'{translated.src.lower()}'].title()
    dest_lang = LANGUAGES[f'{translated.dest.lower()}'].title()
    translated_text = translated.text
    msg.reply_text(tld(chat.id,
                       'translator_translated').format(src_lang,
                                                       to_translate_text,
                                                       dest_lang,
                                                       translated_text),
                   parse_mode=ParseMode.MARKDOWN)


__help__ = """
Here is help for translation Module.
- /tr <lang>:  Use this to translate the text.
"""

__mod_name__ = "TRANSLATION"

dispatcher.add_handler(
    DisableAbleCommandHandler("tr", do_translate, pass_args=True))
