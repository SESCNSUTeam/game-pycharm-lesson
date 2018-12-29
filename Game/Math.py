import pygame
def handle_collision_detect(object1, object2):
    return centers_dif(object1.bounds, object2.bounds)

def centers_dif(rect1,rect2):
    return rect2.centerx - rect1.centerx, rect2.centery - rect1.centery
