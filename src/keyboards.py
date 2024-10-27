"""

MADE BY Usanin Andrey a.k.a. Aqamaru
         TG: @NightsForever          
            VK: @Aqamaru            

"""

from text import Button, Quantities, Scale
from telebot.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup

MAIN_MENU = ReplyKeyboardMarkup(resize_keyboard = True)\
        .add(*(KeyboardButton(i) for i in (
            Button.CONVERT,
            Button.CALCULATE,
            Button.SCALING
        )))\
        .add(*(KeyboardButton(i) for i in (
            Button.HELP,
        )))

WHICH_CALCULATE = InlineKeyboardMarkup(row_width = 3)\
        .add(*(InlineKeyboardButton(i[0], i[1]) for i in (
            ()
        )))

def get_convert(data: str = ""):
    convert = InlineKeyboardMarkup(row_width = 3)
    if data == "":
        convert.add(*(InlineKeyboardButton(
                text = i[0], callback_data = f"convert_from_{i[1]}_to_") 
                    for i in QUANTITIES
                    )
                )
    else:
        convert.add(*(InlineKeyboardButton(
                text = i[0], callback_data = data + f"{i[1]}") 
                    for i in QUANTITIES
                    )
                )
    convert.add(InlineKeyboardButton(text = Button.MEANINGS, callback_data = "convert_meanings"))
    return convert

def get_scale(data: str = "" ,is_positive: bool = True) -> InlineKeyboardMarkup:
    scales = InlineKeyboardMarkup(row_width = 3)
    if data == "":
        if is_positive:
            scales.add(*(InlineKeyboardButton(
                    text = i[0], callback_data = f"scale_from_{i[1]}_to_")
                        for i in SCALES_POSITIVE
                        )
                    )
            scales.add(InlineKeyboardButton(
                    text = "-", callback_data = "scale_from_none_to_"
                        )
                    )
            scales.add(InlineKeyboardButton(
                    text = "🔄", callback_data = "scale_negative"
                        )
                    )
            return scales
        
        scales.add(*(InlineKeyboardButton(
                text = i[0], callback_data = f"scale_from_{i[1]}_to_")
                    for i in SCALES_NEGATIVE
                    )
                )
        scales.add(InlineKeyboardButton(
                text = "-", callback_data = "scale_from_none_to_"
                    )
                )
        scales.add(InlineKeyboardButton(
                text = "🔄", callback_data = "scale_positive"
                    )
                )
        return scales
    
    if is_positive:
        scales.add(*(InlineKeyboardButton(
                text = i[0], callback_data = data + f"{i[1]}")
                    for i in SCALES_POSITIVE
                    )
                )
        scales.add(InlineKeyboardButton(
                text = "-", callback_data = data + "none"
                    )
                )
        scales.add(InlineKeyboardButton(
                text = "🔄", callback_data = data + "negative"
                    )
                )
        return scales
    
    scales.add(*(InlineKeyboardButton(
            text = i[0], callback_data = data + f"{i[1]}")
                for i in SCALES_NEGATIVE
                )
            )
    scales.add(InlineKeyboardButton(
            text = "-", callback_data = data + "none"
                )
            )
    scales.add(InlineKeyboardButton(
            text = "🔄", callback_data = data + "positive"
                )
            )
    return scales

QUANTITIES = (
        (Quantities.WAVEIFREQUENCY, Quantities.WAVEIFREQUENCY._name_.lower()),
        (Quantities.WAVEILENGHT, Quantities.WAVEILENGHT._name_.lower()),
        (Quantities.PHOTONIENERGY, Quantities.PHOTONIENERGY._name_.lower())
        )

SCALES_POSITIVE = (
            (Scale.DECA, Scale.DECA._name_.lower()),
            (Scale.HECTO, Scale.HECTO._name_.lower()),
            (Scale.KILO, Scale.KILO._name_.lower()),
            (Scale.MEGA, Scale.MEGA._name_.lower()),
            (Scale.GIGA, Scale.GIGA._name_.lower()),
            (Scale.TERA, Scale.TERA._name_.lower()),
            (Scale.PETA, Scale.PETA._name_.lower()),
            (Scale.EXA, Scale.EXA._name_.lower()),
            (Scale.ZETTA, Scale.ZETTA._name_.lower()),
            (Scale.YOTTA, Scale.YOTTA._name_.lower()),
            (Scale.RONNA, Scale.RONNA._name_.lower()),
            (Scale.QUETTA, Scale.QUETTA._name_.lower())
        )

SCALES_NEGATIVE = (
            (Scale.DECI, Scale.DECI._name_.lower()),
            (Scale.CENTI, Scale.CENTI._name_.lower()),
            (Scale.MILI, Scale.MILI._name_.lower()),
            (Scale.MICRO, Scale.MICRO._name_.lower()),
            (Scale.NANO, Scale.NANO._name_.lower()),
            (Scale.PICO, Scale.PICO._name_.lower()),
            (Scale.FEMTO, Scale.FEMTO._name_.lower()),
            (Scale.ATTO, Scale.ATTO._name_.lower()),
            (Scale.ZEPTO, Scale.ZEPTO._name_.lower()),
            (Scale.YOCTO, Scale.YOCTO._name_.lower()),
            (Scale.RONTO, Scale.RONTO._name_.lower()),
            (Scale.QUECTO, Scale.QUECTO._name_.lower())
        )
