import pygame


player_str = 10     # strength
player_int = 10     # intellect
player_agi = 16     # agility
player_vit = 10     # vitality
player_speed = player_agi*16
player_hp = player_str*10
player_mp = player_int*5
player_stamina = player_str/2 + player_vit * 5

player_str_growth = 1
player_agi_growth = 1
player_int_growth = 1
player_vit_growth = 1

player_image = None
player_width = 16
player_height = 16

brick_image = None
brick_width = 48
brick_height = 16

mob_image = None
mob_width = 16
mob_height = 16

bullet_image = None
bullet_width = 8
bullet_height = 8

event_spell = pygame.USEREVENT + 1
event_scroll = pygame.USEREVENT + 2
event_calculate_behavior = pygame.USEREVENT + 3
