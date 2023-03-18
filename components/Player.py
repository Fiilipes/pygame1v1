import pygame

class Player:
    def __init__(self, image, screen_size, ground_height):
        self.gravitation = 0
        self.inair = False
        self.running = False
        self.falling = False
        self.left = False
        self.index = 0
        self.surf = pygame.transform.scale_by(pygame.image.load(image), 4)
        self.rect = self.surf.get_rect(midbottom=(screen_size[0]//4, ground_height))

