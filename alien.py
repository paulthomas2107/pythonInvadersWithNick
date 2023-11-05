import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, type_suffix, x, y):
        super().__init__()
        self.type = type
        path = f'Graphics/alien_{type_suffix}.png'
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft=(x, y))