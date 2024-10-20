"""

MADE BY Usanin Andrey a.k.a. Aqamaru
         TG: @NightsForever          
            VK: @Aqamaru            

"""

import telebot

from telebot.types import Message
from main import cfg
from text import Text, Button

cfg.read("config.ini")

BOT = telebot.TeleBot(cfg.get("settings", "tg_token"))

@BOT.message_handler(commands = ["start"])
def on_start(msg: Message) -> None:
   BOT.send_message(chat_id = msg.chat.id, text = Text.GREETINGS,
                    reply_markup = None)

@BOT.message_handler()
def on_message(msg: Message) -> None:
    match msg.text:
        
        case _:
            BOT.send_message(chat_id = msg.chat.id, text = Text.UNKNOWN_COMMAND,
                             reply_markup = None)



def start_bot() -> None:
    BOT.enable_save_next_step_handlers(delay = 2)
    BOT.load_next_step_handlers()
    BOT.infinity_polling()
