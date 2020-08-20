import pygame.font
from pygame.sprite import Group

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, ya_game):
        """Initialize scorekeeping attributes"""
        self.ya_game = ya_game

        self.screen = ya_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ya_game.settings
        self.stats = ya_game.game_stats

        # Font settings for scoring info
        self.text_colour = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.level = self.stats.level
        self.level_str = str(self.level)
        self.health = self.stats.health
        self.health_str = str(self.health)

        # Prepare the initial score image
        self.prep_health()
        self.prep_level()
        #self.prep_game1()
        #self.prep_game2()

    def prep_health(self):
        """Turn the score into a rendered image"""
        if self.health%1 == 0:
            self.health_str = str(self.health)
        self.health_image =self.font.render(self.health_str, True,
                self.text_colour, self.settings.bg_colour)

        # Rendering the word score
        health_word = "Health: "
        self.health_word_image = self.font.render(health_word, True,
                self.text_colour, self.settings.bg_colour)

        # Display the score at the top right of the screen
        self.health_rect = self.health_image.get_rect()
        self.health_rect.right = self.settings.screen_width/3
        self.health_rect.bottom = self.settings.screen_height - self.health_rect.height
        self.health_word_rect = self.health_word_image.get_rect()
        self.health_word_rect.right = self.health_rect.left
        self.health_word_rect.bottom = self.health_rect.bottom

    def prep_level(self):
        # level display
        if self.health % 1 == 0:
            self.level_str = self.level_str

        self.level_image = self.font.render(self.level_str, True,
                                             self.text_colour, self.settings.bg_colour)

        level_word = "Level: "
        self.level_word_image = self.font.render(level_word, True,
                                                 self.text_colour, self.settings.bg_colour)

        # Display the score at the top right of the screen
        self.level_word_rect = self.level_word_image.get_rect()
        self.level_word_rect.left = self.settings.screen_width*(2/3)
        self.level_word_rect.bottom = self.health_rect.bottom
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.level_word_rect.right
        self.level_rect.bottom = self.health_rect.bottom

    def prep_game1(self):
        """Turn the level into a rendered image"""
        game_str1 = str(self.stats.player1_game)
        self.game_image1 = self.font.render(game_str1, True, self.text_colour, self.settings.bg_colour)

        # Position the level to the bottom of the screen
        self.game_rect1 = self.game_image1.get_rect()
        width, height = self.game_rect1.size
        self.game_rect1.x = self.settings.screen_width/3
        self.game_rect1.y = self.settings.screen_height - height

    def prep_game2(self):
        """Turn the level into a rendered image"""
        game_str2 = str(self.stats.player2_game)
        self.game_image2 = self.font.render(game_str2, True, self.text_colour, self.settings.bg_colour)

        # Position the level to the bottom of the screen
        self.game_rect2 = self.game_image2.get_rect()
        width, height = self.game_rect2.size
        self.game_rect2.x = self.settings.screen_width*(2/3)
        self.game_rect2.y = self.game_rect1.y

    def show_game1(self):
        """Draw the scoreboard"""
        self.screen.blit(self.game_image1, self.game_rect1)

    def show_game2(self):
        """Draw the scoreboard"""
        self.screen.blit(self.game_image2, self.game_rect2)

    def show_health(self):
        """Draw the scoreboard"""
        self.screen.blit(self.health_image, self.health_rect)
        self.screen.blit(self.health_word_image, self.health_word_rect)

    def show_level(self):
        """Draw the scoreboard"""
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.level_word_image, self.level_rect)

    def update_health(self):
        self.health = self.stats.health
