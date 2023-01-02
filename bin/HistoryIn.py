# -*- coding:UTF-8 -*-
import sqlite3
import time
import datetime
from Users import *
from HistoryIn import *

conn = sqlite3.connect("stock.db")
c = conn.cursor()

def initHistoryIn():
        c.execute("CREATE TABLE IF NOT EXISTS historyIn (idCarte INTEGER, credit REAL, timestamp VARCHAR)")


def historyIn(carte, credit):
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H: %M:%S'))
    c.execute("INSERT INTO historyIn (idCarte, credit, timestamp) VALUES (?, ?, ?)",
              (carte, credit, date))
    conn.commit()
    print("Ajout dans l'historique ...")
