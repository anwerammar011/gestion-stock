#-*- coding:UTF-8 -*-
import sqlite3
import easygui as eg
from HistoryIn import *
from HistoryStock import *
from Users import *

conn = sqlite3.connect("stock.db")
c = conn.cursor()

def initStock():
    c.execute("CREATE TABLE IF NOT EXISTS stock (idProduit INTEGER, desc VARCHAR, prix REAL, stock INTEGER )")

def ajouterProduit():
    c.execute ('SELECT COUNT(*) FROM stock')
    data = c.fetchone()
    idProduit = data[0]+1
    desc = eg.enterbox(msg="Entrez le nom du produit : ",title="Ajout")
    prix = eg.enterbox(msg="Entrez le prix : ",title="Ajout")
    stock = eg.enterbox(msg="Combien de stock ? : ",title="Ajout")

    c.execute("INSERT INTO stock (idProduit, desc, prix, stock) VALUES ( ?, ?, ?, ?)",
        (idProduit, desc, prix, stock))
    conn.commit()
    eg.msgbox(msg="Produit ajouté !")
    historyStock(idProduit, stock)

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

def ajouterStock():
    produit = eg.enterbox(msg="Quel est le nom du produit a stocker ? : ", title="Produit")
    c.execute (f"SELECT desc, stock, idProduit FROM stock WHERE desc = '{produit}'")
    fetched_produit = c.fetchone()
    if fetched_produit:
        quest = f"Le stock contient {fetched_produit[1]} {fetched_produit[0]}. Voulez vous restocker ?"
        rep = eg.ynbox(msg=quest)
        if rep:
            rajout = int(eg.enterbox(msg="Combien de stock a rajouter ? ", title="Rajout"))
            stock = fetched_produit[1]
            stock += rajout
            stock = str(stock)
            c.execute(f"UPDATE stock SET stock = '{stock}' WHERE desc = '{produit}'")
            conn.commit()
            idProduit = fetched_produit[2]
            historyStock(idProduit, rajout)
    else:
        eg.msgbox(msg=f"Impossible de trouver le produit: {produit}",title="Erreur")

    
    
    
    

def consulterStock():
    c.execute("SELECT desc, stock FROM stock")
    total = ""
    for row in c.fetchall():
        temp = str(row[0])
        for i in range(20-len(row[0])):
            temp+=" "
        temp += str(row[1])
        temp = temp + "\n"
        total+= temp
    eg.textbox(text=total, title="Stock")

