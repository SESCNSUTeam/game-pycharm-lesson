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
