from re import M
import pyxel
import random
from algos import calcul_bien_et_mal_places

class Config:
    def __init__(self):
        self.NB_PIONS = 4
        self.COULEURS = [4, 5, 7, 9, 10, 11, 13, 8]

config = Config()

class Choisisseur:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rayon = 6
        self.espacement = self.rayon*2 + 2
        self.click_sur_fait = False

    def update(self, comb_en_cours):
        self.click_sur_fait = False
        # regarde si on clique sur une couleur
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 0 <= pyxel.mouse_y <= self.rayon*2:  # regarde la hauteur
                # ajoute un pion
                if len(comb_en_cours.couleurs) < config.NB_PIONS:
                    for pion in range (len(config.COULEURS)):
                        x_min = 0 + self.espacement*pion
                        x_max = x_min + self.espacement
                        if x_min <= pyxel.mouse_x <= x_max:
                            couleur = config.COULEURS[pion]
                            comb_en_cours.couleurs.append(couleur)
                            break
                # suppr un pion
                retour_x = self.espacement*len(config.COULEURS)
                if retour_x <= pyxel.mouse_x <= retour_x + self.espacement:
                    if len(comb_en_cours.couleurs) > 0:
                        comb_en_cours.couleurs.pop()
                fait_x = retour_x + self.espacement
                if fait_x <= pyxel.mouse_x <= fait_x + self.espacement:
                    self.click_sur_fait = True

    def draw(self, comb_en_cours):
        # affice la liste des couleurs cliquables
        for i, couleur in enumerate(config.COULEURS):
            pyxel.circ(self.x + i*(self.espacement) + self.rayon, self.y + self.rayon, self.rayon, couleur)
        retour_x = self.espacement*len(config.COULEURS)
        pyxel.blt(retour_x, 0, 0, 0, 0, 15, 15)
        if len(comb_en_cours.couleurs) == config.NB_PIONS:
            pyxel.blt(retour_x + self.espacement, 0, 1, 0, 0, 15, 15)


class Combinaison:
    def __init__(self):
        self.couleurs = []
        self.bien_places = 0
        self.mal_places = 0

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
        
        for note in range(self.bien_places):
            pyxel.circ(x+note*9+config.NB_PIONS*15, y, 3, 2)
        for note in range(self.mal_places):
            pyxel.circ(x-note*9-1*15, y, 3, 7)
            
    def __str__(self):
        return f"{str(self.couleurs)} {self.bien_places} {self.mal_places}"

    def compare(self, autre):
        calcul_bien_et_mal_places(self, autre)


class App:
    def __init__(self):
        self.comb_a_trouver = Combinaison()
        self.comb_a_trouver.rand()
        self.anciennes_comb = []
        self.comb_en_cours = Combinaison()
        self.choisisseur = Choisisseur()

        pyxel.init(256, 256, title="Mon Mastermind")
        pyxel.load("mastermind.pyxres", True)
        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.choisisseur.update(self.comb_en_cours)
        if self.choisisseur.click_sur_fait:
            # noter la combinaison
            self.comb_en_cours.compare(self.comb_a_trouver)
            # sauver la comb
            self.anciennes_comb.append(self.comb_en_cours)
            # effacer la comb en cours
            self.comb_en_cours = Combinaison()

        #self.compare_combinaison(self.comb_a_trouver, self.comb_en_cours)

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def compare_combinaison(self, c1, c2):
        print(f"compare {c1} et {c2}")
        for ic1, couleur_c1 in enumerate(c1.couleurs):
            print(f"c1 contient la couleur {couleur_c1=} à {ic1=}")
            for ic2, couleur_c2 in enumerate(c2.couleurs):
                if c2.couleurs[ic2] == couleur_c1:
                    print(f"  c2 aussi, à la position {ic2=}")

    def genere_combinaison(self):
        print(config.NB_PIONS)

    def draw(self):
        pyxel.cls(0)
        for i, ancienecomb in enumerate(self.anciennes_comb):
            ancienecomb.draw(100, 220-15-i*15)


        self.choisisseur.draw(self.comb_en_cours)

        pyxel.text(55, 41, f"Mastermind {pyxel.mouse_x},{pyxel.mouse_y},{pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)}", pyxel.frame_count % 16)

        self.comb_a_trouver.draw(100, 100)
        self.comb_en_cours.draw(100, 220)


App()
