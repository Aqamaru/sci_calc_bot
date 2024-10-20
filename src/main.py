"""

MADE BY Usanin Andrey a.k.a. Aqamaru
         TG: @NightsForever          
            VK: @Aqamaru            

"""

from configparser import ConfigParser
import os

cfg = ConfigParser()

def start():
    if not os.path.isfile("./config.ini"):
        with open("./config.ini", "x", encoding="UTF-8") as config:
            config.write("""
; MADE BY Usanin Andrey a.k.a. Aqamaru
;          TG: @NightsForever          
;             VK: @Aqamaru            

;Настройки БД, в качестве СУБД использовать MariaDB
[database]
;ip
host:
;user name
user:
;password
password:
;database name
dbname:

[settings]
;вставьте здесь токен (https://t.me/BotFather)
tg_token:

;Последующие пункты лучше не изменять
;Все последующие действия будут на ваш риск и ответственность

ver: 0.0.1 
""")
        print("FILL CONFIG")
        return
    cfg.read("./config.ini")
    if cfg.get("database", "host") == "":
        print("ENTER DB IP")
        print(cfg.get("database", "host"))
        return
    if cfg.get("database", "user") == "":
        print("ENTER DB USER")
        return
    if cfg.get("database", "password") == "":
        print("ENTER DB PASSWORD")
        return
    if cfg.get("database", "dbname") == "":
        print("ENTER DB NAME")
        return
    if cfg.get("settings", "tg_token") == "":
        print("ENTER TG TOKEN")
        return
    import bot
    bot.start_bot()

if __name__ == "__main__":
    start()
