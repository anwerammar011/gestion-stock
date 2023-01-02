# -*- coding:UTF-8 -*-
import sqlite3
import time
import easygui as eg
from HistoryIn import *

conn = sqlite3.connect("stock.db")
c = conn.cursor()

def initUsers():
    c.execute("CREATE TABLE IF NOT EXISTS users (idCarte INTEGER, solde REAL, nom VARCHAR)")

def tradCarte(temp):
    res = []
    resInt = 0
    for i in range(len(temp)):
        if temp[i] == "&" or temp[i] == "1":
            res.append(1)
        elif temp[i] == "é" or temp[i] == "2":
            res.append(2)
        elif temp[i] == '"' or temp[i] == "3":
            res.append(3)
        elif temp[i] == "'" or temp[i] == "4":
            res.append(4)
        elif temp[i] == "(" or temp[i] == "5":
            res.append(5)
        elif temp[i] == "-" or temp[i] == "6":
            res.append(6)
        elif temp[i] == "è" or temp[i] == "7":
            res.append(7)
        elif temp[i] == "_" or temp[i] == "8":
            res.append(8)
        elif temp[i] == "ç" or temp[i] == "9":
            res.append(9)
        elif temp[i] == "à" or temp[i] == "0":
            res.append(0)
        else:
            res.append(temp[i])
    for i in range(len(res)):
        resInt += res[len(res)-i-1]*10**i
    return(resInt)

def ajouterUtilisateur():
    temp = eg.enterbox(msg="Passez une carte vierge")
    if temp is not None:
        carte = str(tradCarte(temp))
        count = c.execute (f'SELECT COUNT(idCarte) FROM users WHERE idCarte = {carte}').fetchone()
        
        if count[0] > 0 :
            eg.msgbox(msg="Il y a déjà un utilisateur enregistré sur cette carte !")
        else:
            nom = eg.enterbox(msg="Nom de l'utilisateur", title="Enregistrement")
            if nom is not None:
                solde = eg.enterbox(msg="Solde de l'utilisateur", title="Enregistrement")
                if solde == '' : solde = 0
                c.execute("INSERT INTO users (idCarte, solde, nom) VALUES ( ?, ?, ?)", (carte, solde, nom))
                conn.commit()
                eg.msgbox(msg="Utilisateur ajouté !", title="Succès !")
                historyIn(carte, solde)
                time.sleep(1)

def consulterSolde():
    temp = eg.enterbox(msg="Passez une carte ...")
    if temp:
        carte = str(tradCarte(temp))
        compte = c.execute (f'SELECT nom, solde FROM users WHERE idCarte = {carte}').fetchone()
        if compte is None :
            eg.msgbox(msg="Utilisateur introuvable!")
        else:
            msg_solde = f"Le solde est de : {compte[1]} Euros \nLa carte appartient à {compte[0]}"
            eg.msgbox(msg=msg_solde, title='Solde')

def crediterUtilisateur():
    temp = eg.enterbox(msg="Passez une carte ...")
    carte = str(tradCarte(temp))
    credit= float(eg.enterbox(msg="Combien à crediter ?"))
    solde = c.execute (f'SELECT solde FROM users WHERE idCarte = {carte}').fetchone()
    new_credit = str(solde[0] - credit)
    c.execute(f"UPDATE users SET solde = '{new_credit}' WHERE idCarte = {carte}")
    conn.commit()
    msg_total = f"Le credit est à présent de : {new_credit}"
    historyIn(carte, credit)
    eg.msgbox(msg=msg_total, title="Mise a jour")
    time.sleep(1)
