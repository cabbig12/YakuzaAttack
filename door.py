import pygame

class Door:
    """A class to control the behaviour and assets of the door"""

    def __init__(self, ya_game):
        """Initialize attributes of the class"""
        super(Door, self).__init__()
        self.screen = ya_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ya_game.settings
        self.game_stats = ya_game.game_stats

        # Load the door's image and get the rect
        self.image = pygame.image.load('images/door.PNG')
        self.rect = self.image.get_rect()
        self.x = self.rect.x

    def blitme(self):
        """Draw the hero at its current location"""
        self.screen.blit(self.image, self.rect)