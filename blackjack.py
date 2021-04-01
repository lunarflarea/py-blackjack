# Blackjack
# règles : http://fr.wikipedia.org/wiki/Blackjack_(jeu)
# voici à quoi doit ressembler le jeu : https://gyazo.com/7b1e9c4517ae5b6f9da99c2944236e1a

from random import randrange
from tkinter import *
from time import sleep

couleur = ('pique', 'trefle', 'carreau', 'coeur')
valeur = ('as', '2', '3', '4', '5', '6', '7',
          '8', '9', '10', 'valet', 'dame', 'roi')


# TODO calculer la main du croupier ou du joueur en fonction des cartes tirées par l'un ou l'autre
def calculer_main(cartes):
    total = 0
    for i in range(0, cartes.len):
        total+=carte[i].valeur
        return total


class Carte:  # la classe Carte, c'est cadeau
    def __init__(self, val='as', coul='carreau'):
        self.valeur = val
        self.couleur = coul

    def dessin_carte(self):
        # Renvoi l'image de la carte, les images sont dans le dossier "cartes"
        nom = "cartes/"+self.valeur+"_"+self.couleur+".gif"
        return PhotoImage(file=nom)


class Joueur:
    # Main du joueur

    def __init__(self):
        self.main = []

    def ajouter(self, c):
        # TODO Ajouter la carte c à sa main

    def total(self):
        # TODO Calculer le total des points de la main

    def nb_cartes(self):
        return len(self.main)

    def reinit(self):
        self.main = []


class Paquet_de_cartes:
    # Paquet de cartes

    def __init__(self):
        # TODO Construction de la liste des 52 cartes en utilisant la classe Carte(valeur,couleur)
        self.cartes = []

    def melanger(self):
        # TODO Mélanger les cartes

    def tirer(self):
        # TODO Tirer la première carte de la pile et la retirer du tableau des cartes pour qu'elle ne soit plus tirée
        return


def reinit():
    global mes_cartes, ses_cartes, mon_score, son_score, moi, croupier
    global jeu, can

    can.delete(ALL)
    can.create_text(60, 30, text="Croupier", fill='black', font='Arial 18')
    can.create_text(60, 470, text="Joueur", fill='black', font='Arial 18')
    can.update()

    # TODO reinitialiser la partie via le croupier, reset le paquet de cartes et les mains,
    # TODO mélanger les cartes et tirer 1 carte pour le croupier puis 2 pour le joueur
    # TODO attention à bien mettre à jour les mains de chaque joueurs + calculer les scores + afficher les cartes et le resultat dans la fenêtre TK Inter

    can.update()

    # TODO verifier si j'ai fait un blackjack pour savoir si j'ai gagné la partie
    # TODO afficher un message "gagné du côté de mon côté" puis réinitialiser la partie après 3 secondes


def hit():  # le joueur tire une carte
    global mes_cartes, moi, mon_score, son_score
    # TODO tirer la carte et l'ajouter à ma main
    n = moi.nb_cartes()
    can.create_image(150+50*(n-2), 350, image=mes_cartes[n-1])
    can.delete(mon_score)
    mon_score = can.create_text(150, 470, text=str(
        moi.total()), fill='black', font='Arial 18')
    can.update()
    # TODO verifier si j'ai perdu, afficher un message "gagné du côté du croupier" puis réinitialiser la partie après 3 secondes


def stay():  # le joueur s'arrête de jouer alors c'est le croupier qui joue solo. Ici, faire une fonction récursive
    global ses_cartes, croupier, moi, son_score, mon_score
    # TODO tirer une carte pour le croupier, ajouter à sa main et afficher la carte tirée et son score total
    can.update()
    # TODO verifier les scores du croupier pour savoir s'il va rejouer ou non et comparer son score à notre score pour savoir qui gagne
    # TODO voir si c'est nous qui gagnons, afficher le message et réintialiser la partie après 3 secondes


# fenetre graphique (rien à toucher ! elle est déjà prète, c'est cadeau)
moi = Joueur()
mes_cartes = []
croupier = Joueur()
ses_cartes = []
jeu = Paquet_de_cartes()
fenetre = Tk()
fenetre.title("Blackjack")
can = Canvas(fenetre, width=600, height=500, bg='white')
can.pack(side=TOP, padx=5, pady=5)
b2 = Button(fenetre, text='Quitter', width=15, command=fenetre.quit)
b2.pack(side=RIGHT)
b1 = Button(fenetre, text='Carte !', width=15, command=hit)
b1.pack(side=LEFT)
b1 = Button(fenetre, text='Je reste', width=15, command=stay)
b1.pack(side=LEFT)
reinit()

# demarrage :
fenetre.mainloop()
fenetre.destroy()
