import pygame

player_str = 10  # strength
player_int = 10  # intellect
player_agi = 16  # agility
player_vit = 10  # vitality

player_speed = player_agi * 16
player_hp = player_str * 10
player_mp = player_int * 5
player_stamina = player_str / 2 + player_vit * 5

player_str_growth = 1
player_agi_growth = 1
player_int_growth = 1
player_vit_growth = 1

image_player = None
width_player = 16
height_player = 16

image_brick = None
width_brick = 48
height_brick = 16

image_mob = None
width_mob = 16
height_mob = 16

image_bullet = None
width_bullet = 8
height_bullet = 8

image_dict = dict()

event_spell = pygame.USEREVENT + 1
event_scroll = pygame.USEREVENT + 2
event_calculate_behavior = pygame.USEREVENT + 3


def init():
    image_dict[0] = None
    image_dict[1] = image_brick
    image_dict[2] = image_mob
    image_dict[3] = image_player
    image_dict[4] = image_bullet

