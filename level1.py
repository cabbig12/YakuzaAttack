import pygame
from pygame.sprite import Sprite

class Level1(Sprite):

    def __init__(self, ya_game, width, x, y):
        super(Level1, self).__init__()
        self.screen = ya_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ya_game.settings
        self.colour = self.settings.floor_colour
        height = self.settings.floor_height
        self.floor_widths = [1000, 120, 250, 870, 1120, 1200]

        # Building a floor
        self.floor = pygame.Surface([width, height])
        self.floor.fill(self.colour)
        self.floor.set_colorkey(self.colour)
        self.rect = self.floor.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_platforms(self):
        pygame.draw.rect(self.screen, self.settings.floor_colour, self.rect)