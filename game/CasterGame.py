from Game.game.MyGame import Game
from Game.game.Player import Player


class SpellCaster(Game):
    def __init__(self,
                 caption,
                 width,
                 height,
                 player):
        Game.__init__(self, caption, width, height, "..//resources//black.png", 60)
        self.player = player

    def update(self, dt):
        self.player.update(dt)

    def draw(self):
        self.player.draw(self.surface)


def play():

    player = Player(5, 5, "..//resources//green.png")
    game = SpellCaster("SpellCaster", 1280, 720, player)
    game.run()

play()