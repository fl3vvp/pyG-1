import pygame
from main import *

# Classe base para objetos do jogo
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # nós usaremos isso mais tarde
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        # sub-classes devem sobrescrever
        pass