import pygame
from pygame.sprite import Sprite

class Hero(Sprite):
    """A class to control the behaviour and attributes of the hero"""
    def __init__(self, ya_game):
        """Intialize the hero and set its starting position"""
        super(Hero, self).__init__()
        self.screen = ya_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ya_game.settings

        # Load the hero's image and get the rect
        self.image = pygame.image.load('images/lana_hero.PNG')
        self.rect = self.image.get_rect()

        # Start each the hero at the bottom center of the screen.
        self.rect.midbottom = (20, 137)

        # Store decimal for the hero's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.looking_left = False
        self.looking_right = False
        self.super_jump = False
        self.normal_jump = False
        self.jump_finished = False

    def update(self):
        """Update the ships position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            pygame.transform.flip(self.image, True, False)
            self.x += self.settings.hero_speed

        if self.moving_left and self.rect.left > 0:
            pygame.transform.flip(self.image, False, False)
            self.x -= self.settings.hero_speed

        # Update the rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the hero at its current location"""
        self.screen.blit(self.image, self.rect)
    def reposition_hero(self):
        """Reposition the hero 5 pixels away"""
        if self.moving_right:
            self.x -= 5
            self.rect.x = self.x
        elif self.moving_left:
            self.x += 5
            self.rect.x = self.x