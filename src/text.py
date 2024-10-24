"""

MADE BY Usanin Andrey a.k.a. Aqamaru
         TG: @NightsForever          
            VK: @Aqamaru            

"""

from enum import Enum

class Text(str, Enum):
    GREETINGS = ("Здравствуйте!\n"
                 "Это бот-калькулятор.")
    
    WHICH_CONVERT = ("Какую величину вы хотите перевести?")

    WHICH_CALCULATE = ("Какую величину вы хотите вычислить?")

    WHICH_SCALE_FROM = ("Какая приставка Си у вас есть?")

    WHICH_SCALE_TO = ("Какую приставку Си хотите получить?")
    
    SCALE_GET_NUM = ("Введите числовое значение:\n"
                     "Поддерживается ввод чисел в виде x*10^n")

    SCALE_FINAL = ("Результат: %n %pЕд.")

    HELP = ("Выберите раздел для получения информации о нём:")

    UNKNOWN_COMMAND = ("Неизвестная команда.\n"
                       "Проверьте корректность ввода.")


class Button(str, Enum):
    CONVERT = ("Перевод")

    CALCULATE = ("Вычисление")

    SCALING = ("Масштабирование")

    HELP = ("Помощь")
    
    BACK = ("Назад")

    BACK_TO_MAIN_MENU = ("Вернуться в меню")

class Scale(str, Enum):
    DECA = ("да")
    HECTO = ("г")
    KILO = ("к")
    MEGA = ("М")
    GIGA = ("Г")
    TERA = ("Т")
    PETA = ("П")
    EXA = ("Э")
    ZETTA = ("З")
    YOTTA = ("И")
    RONNA = ("Рн")
    QUETTA = ("Кв")
    
    DECI = ("д")
    CENTI = ("с")
    MILI = ("м")
    MICRO = ("мк")
    NANO = ("н")
    PICO = ("п")
    FEMTO = ("ф")
    ATTO = ("а")
    ZEPTO = ("з")
    YOCTO = ("и")
    RONTO = ("рн")
    QUECTO = ("кв")

