import time
import os
import easygui as eg

from Users import *
from HistoryIn import *
from Stock import *
from Sell import *
from HistoryOut import *
from Bonus import *

initUsers()
initHistoryIn()
initStock()
initHistoryStock()
initHistoryOut()
initBonus()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def afficheMenu():
    listeActions = ["Vente","Ajouter Utilisateur","Crediter Utilisateur", "Consulter Utilisateur", "Ajouter Produit", "Ajouter Stock", "Consulter Stock", "Sauvegarder & Quitter"]
    data = eg.choicebox(msg="Que souhaitez vous faire ?", title="Stock", choices=listeActions)
    launch(data)

def launch(rep):
    if rep == "Vente":
        vendre()
    elif rep == "Ajouter Utilisateur":
        ajouterUtilisateur()
    elif rep == "Crediter Utilisateur":
        crediterUtilisateur()
    elif rep == "Consulter Utilisateur":
        consulterSolde()
    elif rep == "Ajouter Produit":
        ajouterProduit()
    elif rep == "Ajouter Stock":
        ajouterStock()
    elif rep == "Consulter Stock":
        consulterStock()
    elif rep == "Transferer solde Bonus":
        transfererBonus()
    elif rep == "Sauvegarder & Quitter":
        c.close()
        exit()
    else:
        eg.msgbox(msg="Choix inconnu", title="Erreur !")
        time.sleep(2)

while 1:
    afficheMenu()
