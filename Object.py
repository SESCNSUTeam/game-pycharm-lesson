import pygame as pg
class Object:

    def __init__(self, image, x, y, width, height):
        self.image = image;
        self.rectangle = image.get_rect()
        self.speed = [1,1]
        self.width = width
        self.height = height

    def update(self):
        self.rectangle = self.rectangle.move(self.speed)
        if self.rectangle.left < 0 or self.rectangle.right > self.width:
            self.speed[0] = -self.speed[0]

        if self.rectangle.top < 0 or self.rectangle.bottom > self.height:
            self.speed[1] = -self.speed[1]

    def render(self, screen):
        screen.blit(self.image, self.rectangle)