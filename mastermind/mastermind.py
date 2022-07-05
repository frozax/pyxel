import pyxel

class App:
    def __init__(self):
        pyxel.init(256, 256, title="Mastermind")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Mastermind", pyxel.frame_count % 16)
        for rond in range(8):
            pyxel.rect(10 + rond*5, 10 + rond*10, 5, 5, rond+2)

        for cercle in range(4):
            pyxel.circ(80 + 20*cercle, 120, 8, 4)
         
        pyxel.circ(128, 200, 8, 5)
        pyxel.circ(108, 200, 8, 4)


App()
