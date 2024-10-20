"""

MADE BY Usanin Andrey a.k.a. Aqamaru
         TG: @NightsForever          
            VK: @Aqamaru            

"""

from enum import Enum

class Text(Enum, str):
    GREETINGS = ("Здравствуйте!\n"
                 "Это бот-калькулятор.")
     
    UNKNOWN_COMMAND = ("Неизвестная команда.\n"
                       "Проверьте корректность ввода.")


class Button(Enum, str):
    CONVERT = ("Перевод")

    CALCULATE = ("Вычисление")

    SCALING = ("Масштабирование")

    HELP = ("Помощь")
    
    BACK = ("Назад")

    BACK_TO_MAIN_MENU = ("Вернуться в меню")
