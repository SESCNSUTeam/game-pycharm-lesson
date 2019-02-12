import json
import pygame
from classes.GameObjects import Wall


class Map:

    def __init__(self, map_file):
        with open(map_file, 'r') as mp:
            data = json.load(mp)
        self.width = data["size"]["x"]
        self.height = data["size"]["y"]
        self.pr = pygame.sprite.Group()
        for wall in data["props"]["walls"]:
            w = Wall(wall["left"], wall["top"], wall["width"], wall["height"])
            self.pr.add(w)


map = Map("maps\\map_test.json")