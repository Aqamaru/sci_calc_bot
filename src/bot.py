"""

MADE BY Usanin Andrey a.k.a. Aqamaru
         TG: @NightsForever          
            VK: @Aqamaru            

"""

import telebot
import keyboards
import utils

from telebot.types import CallbackQuery, Message
from main import cfg
from text import Quantities, Text, Button, Scale

cfg.read("config.ini")

BOT = telebot.TeleBot(cfg.get("settings", "tg_token"))

@BOT.callback_query_handler(func = None)
def on_callback(data: CallbackQuery) -> None:
    if data.data is None:
        print('data.data is None')
        return

    if data.message.id is None:
        print('data.message.id is None')
        return

    if data.data.startswith('scale'):
        if data.data == 'scale_positive':
            BOT.edit_message_text(chat_id = data.message.chat.id, message_id = data.message.id,
                                text = Text.WHICH_SCALE_FROM, reply_markup = keyboards.get_scale())
            return

        if data.data == 'scale_negative':
            BOT.edit_message_text(chat_id = data.message.chat.id, message_id = data.message.id,
                                text = Text.WHICH_SCALE_FROM, reply_markup = keyboards.get_scale(is_positive = False))
            return
        
        if data.data.endswith('_') or data.data.endswith('positive'):
            data.data = data.data.replace('positive', '')
            BOT.edit_message_text(chat_id = data.message.chat.id, message_id = data.message.id,
                                  text = Text.WHICH_SCALE_TO, reply_markup = keyboards.get_scale(data = data.data))
            return

        if data.data.endswith('negative'):
            data.data = data.data.replace('negative', '')
            BOT.edit_message_text(chat_id = data.message.chat.id, message_id = data.message.id,
                                  text = Text.WHICH_SCALE_TO, reply_markup = keyboards.get_scale(is_positive = False, data = data.data))
            return
        
        BOT.delete_message(chat_id = data.message.chat.id, message_id = data.message.id)
        message = BOT.send_message(chat_id = data.message.chat.id, text = Text.SCALE_GET_NUM,
                                   reply_markup = keyboards.MAIN_MENU)
        BOT.register_next_step_handler(message = message, callback = scale, data = data.data)
        return 
        
    if data.data.startswith('convert'):
        if data.data.endswith('meanings'):
            BOT.send_message(chat_id = data.message.chat.id, text = Text.CONVERT_MEANINGS,
                             reply_markup = None)
            return
        if data.data.endswith('_'):
            BOT.edit_message_text(chat_id = data.message.chat.id, message_id = data.message.id,
                                  text = Text.WHICH_CONVERT_TO, reply_markup = keyboards.get_convert(data.data))
            return
        BOT.delete_message(chat_id = data.message.chat.id, message_id = data.message.id)
        quantity = Quantities[data.data.split('_')[2].upper()].value
        message = BOT.send_message(chat_id = data.message.chat.id, text = Text.CONVERT_ENTER.replace('%q', quantity),
                                   reply_markup = keyboards.MAIN_MENU)
        BOT.register_next_step_handler(message = message, callback = convert, data = data.data)
        return

    return

@BOT.message_handler(commands = ["start"])
def on_start(msg: Message) -> None:
    BOT.send_message(chat_id = msg.chat.id, text = Text.GREETINGS,
                     reply_markup = keyboards.MAIN_MENU)
    return

@BOT.message_handler()
def on_message(msg: Message) -> None:
    match msg.text:
        case Button.CONVERT:
            BOT.send_message(chat_id = msg.chat.id, text = Text.WHICH_CONVERT_FROM,
                             reply_markup = keyboards.get_convert())
            return

        case Button.CALCULATE:
            BOT.send_message(chat_id = msg.chat.id, text = Text.WHICH_CALCULATE,
                             reply_markup = None)
            return

        case Button.SCALING:
            BOT.send_message(chat_id = msg.chat.id, text = Text.WHICH_SCALE_FROM,
                             reply_markup = keyboards.get_scale())
            return

        case Button.HELP:
            BOT.send_message(chat_id = msg.chat.id, text = Text.HELP,
                             reply_markup = None)
            return

        case _:
            BOT.send_message(chat_id = msg.chat.id, text = Text.UNKNOWN_COMMAND,
                             reply_markup = keyboards.MAIN_MENU)
            return

def convert(msg: Message, data: str) -> None:
    if msg.text is None:
        print("msg.text is None")
        return
    if data.count('waveifrequency') == 1 and data.count('photonienergy'):
        message = Text.CONVERT_FINAL\
                .replace('%m', Quantities[data.split('_')[4].upper()].value)\
                .replace('%v', utils.convert(msg.text , data))

        BOT.send_message(chat_id = msg.chat.id, text = message,
                         reply_markup = keyboards.MAIN_MENU)
        return
    message = BOT.send_message(chat_id = msg.chat.id, text = Text.CONVERT_ENTER_VELOCITY,
                                reply_markup = keyboards.MAIN_MENU)
    BOT.register_next_step_handler(message = message, callback = convert_with_velocity,
                                   data = data, quantity_value = msg.text)
    return

def convert_with_velocity(msg: Message, data: str, quantity_value: str):
    if msg.text is None:
        print("msg.text is None")
        return
    message = Text.CONVERT_FINAL\
            .replace('%m', Quantities[data.split('_')[4].upper()].value)\
            .replace('%v', utils.convert(quantity_value , data, msg.text))
    BOT.send_message(chat_id = msg.chat.id, text = message,
                     reply_markup = keyboards.MAIN_MENU)
    return


def scale(msg: Message, data: str) -> None:
    if msg.text is None:
        print("msg.text is None")
        return
    if data.split('_')[4] == 'none':
        message = Text.SCALE_FINAL\
                .replace('%n', utils.scale(msg.text, data))\
                .replace('%p', '')
    else:
        message = Text.SCALE_FINAL\
                .replace('%n', utils.scale(msg.text, data))\
                .replace('%p', Scale[data.split('_')[4].upper()].value)
    BOT.send_message(chat_id = msg.chat.id, text = message,
                     reply_markup = keyboards.MAIN_MENU) 
    return

def start_bot() -> None:
    BOT.enable_save_next_step_handlers(delay = 2)
    BOT.load_next_step_handlers()
    BOT.infinity_polling()
