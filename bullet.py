import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """"A class to manage bullets fired from the ship"""

    def __init__(self, ya_game):
        """Create a bullet object at the ships current position"""
        super(Bullet, self).__init__()
        self.screen = ya_game.screen
        self.settings = ya_game.settings
        self.colour = self.settings.bullet_colour
        self.hero = ya_game.hero

        # Create a bullet at the correct position
        #xpos = ai_game.ship.rect.x
        #ypos = ai_game.ship.rect.y
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ya_game.hero.rect.center

        # Store the bullet's positon as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        if self.hero.looking_right:
            self.x += self.settings.bullet_speed
        elif self.hero.looking_left:
            self.x -= self.settings.bullet_speed

        # Update the rect's position
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)
