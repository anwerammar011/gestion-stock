# -*- coding:UTF-8 -*-
import sqlite3
import time
import datetime
from HistoryIn import *
from HistoryStock import *

conn = sqlite3.connect("stock.db")
c = conn.cursor()

def initHistoryStock():
        c.execute("CREATE TABLE IF NOT EXISTS historyOut (idCarte INTEGER, idProduit, timestamp VARCHAR)")
        c.execute("CREATE TABLE IF NOT EXISTS historyStock (idProduit INTEGER, stock INTEGER, timestamp VARCHAR)")
    

def historyStock(produit, stock):
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H: %M:%S'))
    c.execute("INSERT INTO historyStock (idProduit, stock, timestamp) VALUES (?, ?, ?)",
              (produit, stock, date))
    conn.commit()
    print("Ajout dans l'historique ... OK !")
    time.sleep(1)
