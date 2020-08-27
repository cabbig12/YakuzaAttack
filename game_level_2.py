import pygame
import sys

from settings import Settings
from hero import Hero
from game_stats import GameStats
from level1 import Level1
from time import sleep
from fire import Fire
from yakuza import Yakuza
from door import Door
from scoreboard import Scoreboard
from bullet import Bullet

class GameLevel2:
    """Class to control the level one attributes"""
    def __init__(self, ya_game):
        self.settings = ya_game.settings
        self.screen = ya_game.screen
        self.screen_rect = self.screen.get_rect()
        self.game_stats = ya_game.game_stats

        # Creating the level1 floors
        self._build_floors()

        # instantiate and position fire
        self._build_fires()

        # Creating the yakuza's
        self._build_yakuzas()

        # Creating the door
        self._build_door()

        self._hero_stuff()

        self._build_collisions()

    def _hero_stuff(self):
        self.bullets = pygame.sprite.Group()
        self.hero = Hero(self)
        self.stats = GameStats(self)
        self.hero_sprites = pygame.sprite.Group()
        self.hero_sprites.add(self.hero)

        # Collisions
    def _build_collisions(self):
        self.floor_collisions = pygame.sprite.groupcollide(self.hero_sprites, self.floors, False, False)
        self.bullet_yakuza_collisions = None
        self.collisions2 = pygame.sprite.groupcollide(self.hero_sprites, self.yakuzas, False, False)
        self.normal_jump_distance = 0

    def _build_door(self):
        """Position and build the level door"""
        self.door = Door(self)
        self.door.rect.y = 196
        self.door.rect.x = -100

    def _build_yakuzas(self):
        """Method to create and position yakuzas"""
        self.yakuzas = pygame.sprite.Group()
        self.yakuza1 = Yakuza(self)
        self.yakuza1.rect.y = self.fire2.rect.y - 2
        self.yakuza1.x = 600
        self.yakuzas.add(self.yakuza1)

        self.yakuza2 = Yakuza(self)
        self.yakuza2.rect.y = self.fire4.rect.y - 5
        self.yakuza2.x = 600
        self.yakuzas.add(self.yakuza2)

        self.yakuza3 = Yakuza(self)
        self.yakuza3.rect.y = self.fire3.rect.y - 5
        self.yakuza3.x = 410
        self.yakuzas.add(self.yakuza3)

        self.yakuzas_ghost = self.yakuzas.copy()

    def _build_floors(self):
        """Method to create and position floors"""
        # Creating the level1 floors
        self.floors = pygame.sprite.Group()
        self.floor_widths = [1000, 120, 250, 870, 1120, 1200]
        self.floor0 = Level1(self, self.floor_widths[0], 0, 135)
        self.floors.add(self.floor0)
        self.floor1 = Level1(self, self.floor_widths[1], 1080, 135)
        self.floors.add(self.floor1)
        self.floor2 = Level1(self, self.floor_widths[2], 0, 285)
        self.floors.add(self.floor2)
        self.floor3 = Level1(self, self.floor_widths[3], 330, 285)
        self.floors.add(self.floor3)
        self.floor4 = Level1(self, self.floor_widths[4], 0, 435)
        self.floors.add(self.floor4)
        self.floor5 = Level1(self, self.floor_widths[5], 0, 585)
        self.floors.add(self.floor5)

    def _build_fires(self):
        """Method to create and position fires"""
        # instantiate and position fire
        self.fires = pygame.sprite.Group()
        self.fire1 = Fire(self)
        self.fire1.rect.y = 85 + 18
        self.fire1.x = 500
        self.fire1.rect.x = self.fire1.x
        self.fires.add(self.fire1)

        self.fire2 = Fire(self)
        self.fire2.rect.y = 230 + 23
        self.fire2.x = 150
        self.fire2.rect.x = self.fire2.x
        self.fires.add(self.fire2)

        self.fire3 = Fire(self)
        self.fire3.rect.y = 385 + 18
        self.fire3.x = 770
        self.fire3.rect.x = self.fire3.x
        self.fires.add(self.fire3)

        self.fire4 = Fire(self)
        self.fire4.rect.y = 535 + 18
        self.fire4.x = 400
        self.fire4.rect.x = self.fire4.x
        self.fires.add(self.fire4)

    def initialize_level_settings(self):
        # Creating the level1 floors
        self._build_floors()

        # instantiate and position fire
        self._build_fires()

        # Creating the yakuza's
        self._build_yakuzas()

        # Creating the door
        self._build_door()

        # Creating hero stuff
        self._hero_stuff()

        # Creating collisions
        self._build_collisions()