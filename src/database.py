"""

MADE BY Usanin Andrey a.k.a. Aqamaru
         TG: @NightsForever          
            VK: @Aqamaru

"""

import mariadb

from main import cfg

class Database:
    def __init__(self, host: str, user: str, password: str, dbname: str):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.initDB()

    def initDB(self):
        with mariadb.connect(host=self.host, user=self.user, password=self.password) as database:
            database.cursor().execute(f"""
            CREATE DATABASE IF NOT EXISTS {self.dbname}
            """)

        with mariadb.connect(host=self.host, user=self.user, password=self.password, database=self.dbname) as database:
            database.cursor().execute("""
            CREATE TABLE IF NOT EXISTS survey(
            telegram_id BIGINT,
            mark SMALLINT,
            answer VARCHAR(1000),
            PRIMARY KEY (telegram_id)
            )""")
    
    """

    INSERTERS

    """

    def insert_results(self, telegram_id: int, mark: int, answer: str):
        if telegram_id > 0:
            with mariadb.connect(host=self.host, user=self.user, password=self.password,
                                 database=self.dbname) as database:
                cur = database.cursor()
                cur.execute("""INSERT INTO survey(telegram_id, mark, answer) VALUES(%s, %s, %s)""", (telegram_id, mark, answer))
                return database.commit()

    """

    CHECKERS

    """

    def is_already_passed(self, telegram_id: int):
        if telegram_id > 0:
            with mariadb.connect(host=self.host, user=self.user, password=self.password,
                                 database=self.dbname) as database:
                cur = database.cursor()
                cur.execute("""SELECT telegram_id FROM survey WHERE telegram_id = %s""", (telegram_id,))
                return bool(len(cur.fetchall()))

cfg.read("./config.ini")

DB = Database(
        cfg.get("database", "host"),
        cfg.get("database", "user"),
        cfg.get("database", "password"),
        cfg.get("database", "dbname")
    )
