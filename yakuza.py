import pygame
from pygame.sprite import Sprite
import random

class Yakuza(Sprite):
    """A class to control the attributes and behaviour of the Yakuza"""
    def __init__(self, ya_game):
        """Initialize attributes of the class"""
        super(Yakuza, self).__init__()
        self.screen = ya_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ya_game.settings
        self.game_stats = ya_game.game_stats

        # Load the fire's image and get the rect
        self.image = pygame.image.load('images/yakuza.PNG')
        self.rect = self.image.get_rect()
        self.x = self.rect.x

        # Yakuza movement flag
        self.moving_right = 1
        self.moving_left = 2
        self.dummy = 0

        # yakuza direction options
        self.choices = [self.moving_left, self.moving_right]
        self.choice = random.choice(self.choices)

    def blitme(self):
        """A method to draw the yakuza on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Method to move the yakuza back and fourth along a platform"""
        if self.choice == 1:
            self.x += self.settings.yakuza_speed
            self.rect.x = self.x
            self.dummy += self.settings.yakuza_speed
            if self.dummy >= self.settings.yakuza_distance:
                self.choice = 2
        if self.choice == 2:
            self.x -= self.settings.yakuza_speed
            self.rect.x = self.x
            self.dummy -= self.settings.yakuza_speed
            if self.dummy <= self.settings.yakuza_left_distance:
                self.choice = 1