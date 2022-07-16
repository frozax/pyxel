from re import M
import pyxel
import random

class Config:
    def __init__(self):
        self.NB_PIONS = 4
        self.COULEURS = [4, 5, 7, 9, 10, 11, 13, 8]

config = Config()

class Choisisseur:
    def __init__(self, comb_en_cours):
        self.x = 0
        self.y = 0
        self.rayon = 6
        self.espacement = self.rayon*2 + 2
        self.comb_en_cours = comb_en_cours

    def update(self):
        # regarde si on clique sur une couleur
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 0 <= pyxel.mouse_y <= self.rayon*2:  # regarde la hauteur
                for pion in range (len(config.COULEURS)):
                    x_min = 0 + self.espacement*pion
                    x_max = x_min + self.espacement
                    if x_min <= pyxel.mouse_x <= x_max:
                        couleur = config.COULEURS[pion]
                        self.comb_en_cours.couleurs.append(couleur)
                retour_x = self.espacement*len(config.COULEURS)
                if retour_x <= pyxel.mouse_x <= retour_x + 2*self.espacement:
                    print("retour")

    def draw(self):
        # affice la liste des couleurs cliquables
        for i, couleur in enumerate(config.COULEURS):
            pyxel.circ(self.x + i*(self.espacement) + self.rayon, self.y + self.rayon, self.rayon, couleur)
        retour_x = self.espacement*len(config.COULEURS)
        pyxel.blt(retour_x, 0, 0, 0, 0, 15, 15)


class Combinaison:
    def __init__(self):
        self.couleurs = []

    def rand(self):
        # ici, generer les couleurs dans la variable self.couleurs
        # au lieu de mettre les couleurs 0, 1, 2, 3, les trouver en aléatoire
        # pour ça, utiliser la fonction random.randint(min, max)
        for _ in range(config.NB_PIONS):
            rnd = random.randint(0, len(config.COULEURS)-1)
            self.couleurs.append(config.COULEURS[rnd])
  
        print(self.couleurs)
        
        # pour savoir combien il y a d'elements dans une liste, on peut faire: len(config.COULEURS)

        # exemple pour afficher des nombres au pif entre 0 et 6
        for boucle in range(5):
            print(random.randint(1, 6))

    def draw(self, x, y):
        for i in range (len(self.couleurs)):
            pyxel.circ(x+i*15, y, 5, self.couleurs[i])


class App:
    def __init__(self):
        self.comb_a_trouver = Combinaison()
        self.comb_a_trouver.rand()
        self.comb_en_cours = Combinaison()
        self.choisisseur = Choisisseur(self.comb_en_cours)

        pyxel.init(256, 256, title="Mon Mastermind")
        pyxel.load("mastermind.pyxres", True)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if len(self.comb_en_cours.couleurs) < config.NB_PIONS:
            self.choisisseur.update()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def genere_combinaison(self):
        print(config.NB_PIONS)

    def draw(self):
        pyxel.cls(0)

        self.choisisseur.draw()

        pyxel.text(55, 41, f"Mastermind {pyxel.mouse_x},{pyxel.mouse_y},{pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)}", pyxel.frame_count % 16)

        self.comb_a_trouver.draw(100, 200)
        self.comb_en_cours.draw(100, 220)


App()
