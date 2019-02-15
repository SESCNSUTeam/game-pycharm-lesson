import pygame
user_event = pygame.USEREVENT + 1
QUIT = pygame.QUIT - user_event
KEYDOWN = pygame.KEYDOWN - user_event
KEYUP = pygame.KEYUP - user_event
RESIZE = pygame.VIDEORESIZE - user_event
MOUSEBUTTONDOWN = pygame.MOUSEBUTTONDOWN - user_event
MOUSEBUTTONUP = pygame.MOUSEBUTTONUP - user_event
MOUSEMOTION = pygame.MOUSEMOTION - user_event

event_id_EXIST = 0
event_id_CLICK = 1
event_id_MOVE = 2
event_id_SPAWN = 3
event_id_SPELL = 4

player_str = 10     # strength
player_int = 10     # intellect
player_agi = 10     # agility
player_vit = 10     # vitality
player_speed = player_agi*16
player_hp = player_str*10
player_mp = player_int*5
player_stamina = player_str/2 + player_vit * 5

player_str_growth = 1
player_agi_growth = 1
player_int_growth = 1
player_vit_growth = 1

