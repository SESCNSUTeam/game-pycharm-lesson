import pygame


def spell_request(spell, pos):
    event = pygame.event.Event(pygame.USEREVENT + 1, {"pos": pos, "spell": spell})
    pygame.event.post(event)


def use_scroll_request(scroll, pos):
    event = pygame.event.Event(pygame.USEREVENT + 2, {"pos": pos, "scroll": scroll})
    pygame.event.post(event)
