import pygame
import random
from pygame.sprite import Sprite
from settings import Settings

class Drop(Sprite):
    """A class to represent a single honey drop."""

    def __init__(self, ai_game):
        """Initialize the drop and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('project/images/drop.png')
        self.rect = self.image.get_rect()

        self.rect.y = self.rect.height
        self.rect.x = random.randint(0, self.settings.screen_width)
        self.y = self.rect.y

    def update(self):
        """Move the drop down."""
        self.y += self.settings.drop_speed
        self.rect.y = self.y

    

