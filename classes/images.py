import pygame


def load_image(image):
    try:
        image = pygame.image.load(image)
    except pygame.error as message:
        print('Cannot load image:', image)
        raise SystemExit(message)
    image = image.convert()
    return image


def collide_sprite(sprite, sprite_group, has_sprite=True):
    collide_list = []

    for s in sprite_group:
        if has_sprite:
            if s == sprite:
                has_sprite = False
                continue

        if sprite.global_rect.colliderect(s.global_rect):
            collide_list.append(s)

    return collide_list
