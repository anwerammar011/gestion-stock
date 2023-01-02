# -*- coding:UTF-8 -*-
import sqlite3
import time
import datetime
import random
import os
import easygui as eg

from Users import *
from HistoryIn import *
from Stock import *
from Sell import *
from HistoryOut import *
from Bonus import *

conn = sqlite3.connect("stock.db")
c = conn.cursor()


def beautify(moche):
    beau = ""
    for i in moche:
        beau += str(i)
    return beau

def initBonus():
    c.execute("CREATE TABLE IF NOT EXISTS bonus (idCarte INTEGER, soldeBonus REAL, vip BOOLEAN)")

def transfererBonus():
    temp = eg.enterbox(msg="Passez la carte" , title="Transfer Bonus")
    carte = str(tradCarte(temp))
    c.execute("SELECT soldeBonus FROM bonus WHERE idCarte =" +carte)
    soldeBonus = c.fetchone()
    eg.msgbox(beautify(("Transfert ... OK ! Total transféré ",soldeBonus[0])),"OK" , "OK")
    c.execute("SELECT solde FROM users WHERE idCarte =" +carte)
    solde = c.fetchone()
    tot = solde[0] + soldeBonus[0]
    c.execute("UPDATE bonus SET soldeBonus = 0 WHERE idCarte =" +carte)
    c.execute("UPDATE users SET solde =" + str(tot)+ " WHERE idCarte = "+carte)
    conn.commit()
