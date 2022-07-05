import pyxel

class Config:
    def __init__(self):
        self.NB_PIONS = 4
        self.COULEURS = [4, 5, 7, 9, 10, 11, 13, 8]

class App:
    def __init__(self):
        self.config = Config()
        self.genere_combinaison()

        pyxel.init(256, 256, title="Mon Mastermind")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def genere_combinaison(self):
        print(self.config.NB_PIONS)

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Mastermind", pyxel.frame_count % 16)
        for i, couleur in enumerate(self.config.COULEURS):
            pyxel.circ(5+i*10, 100, 4, couleur)

        # affiche les 4 pions
        for cercle in range(4):
            pyxel.circ(80 + 20*cercle, 120, 8, 5+cercle)


App()
