from GameObject import GameObject
import pygame
class Player(GameObject):
    def __init__(self,x,y,image_dir,speed,acceleration):
        self.image = pygame.image.load(image_dir)
        GameObject.__init__(self,x,y,self.image.get_width(), self.image.get_height(), acceleration, speed)
