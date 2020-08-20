import pygame
from pygame.sprite import Sprite

class Fire(Sprite):
    """A class to control the behaviour and assets of the fire"""
    def __init__(self, ya_game):
        """Initialize attributes of the class"""
        super(Fire, self).__init__()
        self.screen = ya_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ya_game.settings
        self.game_stats = ya_game.game_stats

        # Load the fire's image and get the rect
        self.image = pygame.image.load('images/flame.PNG')
        self.rect = self.image.get_rect()
        self.x = self.rect.x

        self.moving_right = True
        self.moving_left = False
        self.dummy = 0

    def update(self):
        """Alternate the position of the flame"""
        # Alternate the x value to create an animation
        self.x += 3
        self.rect.x = self.x


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
    def flicker_fire(self):
        """Create a flickering animation for the fire"""
        if self.moving_right:
            self.x += 1
            self.rect.x = self.x
            self.dummy += 1
            if self.dummy >= 3:
                self.moving_right = False
                self.moving_left = True
        elif self.moving_left:
            self.x -= 1
            self.rect.x = self.x
            self.dummy -= 1
            if self.dummy == 0:
                self.moving_left = False
                self.moving_right = True
