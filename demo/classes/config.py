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
player_width = 32
player_height = 32

brick_image = None
brick_width = 64
brick_height = 32

# entity_dict = {1: ('player', player_width, player_height), 2: ('brick', brick_width, brick_height)}
spell_THROW = pygame.USEREVENT + 1
spell_SUMMON = pygame.USEREVENT + 2
spell_THROW_AOE = pygame.USEREVENT + 3
