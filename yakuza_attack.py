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

class YakuzaAttack:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.game_stats = GameStats(self)
        self.sb = Scoreboard(self)
        pygame.display.set_caption("Yakuza Attack")

        # Creating the level1 floors
        self._build_floors()

        # instantiate and position fire
        self._build_fires()

        # Creating the yakuza's
        self._build_yakuzas()

        # Creating the door
        self._build_door()

        self.bullets = pygame.sprite.Group()
        self.hero = Hero(self)
        self.stats = GameStats(self)
        self.hero_sprites = pygame.sprite.Group()
        self.hero_sprites.add(self.hero)
        self.floor_collisions = pygame.sprite.groupcollide(self.hero_sprites, self.floors, False, False)
        self.collisions2 = pygame.sprite.groupcollide(self.hero_sprites, self.yakuzas, False, False)
        self.normal_jump_distance = 0

    def _build_door(self):
        """Position and build the level door"""
        self.door = Door(self)
        self.door.rect.y = 196
        self.door.rect.x = -400

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

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self._update_hero()
                self._update_fire()
                self._update_yakuza()
                self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            # Set the right movement flag to true
            self.hero.moving_right = True
            self.hero.looking_right = True
            self.hero.looking_left = False
        if event.key == pygame.K_LEFT:
            # Set the left movement flag to true
            self.hero.moving_left = True
            self.hero.looking_left = True
            self.hero.looking_right = False
        if event.key == pygame.K_UP:
            self.hero.normal_jump = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        if event.key == pygame.K_s:
            # set the super jump movement
            self.hero.super_jump = True
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            # Set the right movement flag to false
            self.hero.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Set the left movement flag to false
            self.hero.moving_left = False
        elif event.key == pygame.K_UP:
            #self.hero.normal_jump = False
            #self.settings.initialize_dynamic_settings()
            pass
        elif event.key == pygame.K_s:
            self.hero.super_jump = False
            self.hero.jump_finished = True
            self._falling()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullet position"""
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_yakuza_collision()
    def _falling(self):
        """gravity code"""
        falling_speed = 3
        # If the hero isn't touching the rects'.
        collisions = pygame.sprite.groupcollide(self.hero_sprites, self.floors, False, False)
        if not collisions and not self.hero.super_jump and not self.hero.normal_jump:
            self.hero.y += falling_speed
            self.hero.rect.y = self.hero.y
            self.hero.update()
            self._update_screen()
        else:
            self.hero.rect.y = self.hero.y
            self.hero.update()
            self._update_screen()

    def _falling2(self):
        """gravity code"""
        falling_speed = 3
        # If the hero isn't touching the rects'.
        collisions = pygame.sprite.groupcollide(self.hero_sprites, self.floors, False, False)
        if self.hero.super_jump and collisions:
            self.hero.y += falling_speed
            self.hero.rect.y = self.hero.y
            self.hero.update()
            self._update_screen()

    def _draw_fires(self):
        """Method to draw each fire"""
        for fire in self.fires:
            fire.flicker_fire()
            fire.blitme()

    def _draw_yakuza(self):
        """Method to draw each yakuza"""
        for yakuza in self.yakuzas:
            yakuza.blitme()

    def _update_yakuza(self):
        """update each yakuza in the sprite"""
        for yakuza in self.yakuzas:
            yakuza.update()

    def _update_fire(self):
        """Method to make the fire flicker"""
        for fire in self.fires:
            fire.update()
            self._draw_fires()
            fire.x -= 3
            fire.rect.x = fire.x
            self._draw_fires()

    def _check_hero_fire_collisions(self):
        """Check if hero and and fire collide"""
        collisions = pygame.sprite.groupcollide(self.hero_sprites, self.fires, False, False)
        collisions2 = pygame.sprite.groupcollide(self.hero_sprites, self.yakuzas, False, False)
        if collisions or collisions2:
            self.sb.health -= 0.5
            self.sb.prep_health()
            self.hero.reposition_hero()

    def _super_jump(self):
        flying_speed = 3
        if self.hero.super_jump:
            self.hero.y -= flying_speed
            self.hero.rect.y = self.hero.y
            self._update_screen()
            if self.floor_collisions:
                self.sb.health -= 1
                self._falling2()
        else:
            self._falling()
        self.hero.update()
        self._check_hero_fire_collisions()

    def _hero_jump(self):
        """Method for the hero jump"""
        if self.hero.normal_jump:
            jumping_speed = 3
            self.settings.hero_speed *= 6
            self.hero.y -= jumping_speed
            self.hero.rect.y = self.hero.y
            self.hero.update()
            self.normal_jump_distance += jumping_speed
            self.settings.initialize_dynamic_settings()
            if self.normal_jump_distance > 68:
                self.hero.normal_jump = False
                self.hero.jump_finished = True
                self._falling()
                self.normal_jump_distance = 0

    def _update_hero(self):
        self._super_jump()
        self._hero_jump()
        self._check_hero_fire_collisions()
        self.hero.update()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets)<1:
            self.settings.number_of_bullets -= 1
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullet position"""
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left <= 0 or bullet.rect.right > self.screen_rect.right:
                self.bullets.remove(bullet)
        self._check_bullet_yakuza_collision()


    def _check_bullet_yakuza_collision(self):
        """Check for any bullets that have hit aliens"""
        # If so, get rid of the bullet and the alien
        collisions1 = pygame.sprite.spritecollideany(
            self.yakuza1, self.bullets)

        if collisions1 and self.settings.yakuza1_health > 0:
            self.settings.yakuza1_health -= 1
            print(collisions1)
            print(self.settings.yakuza1_health)
        elif self.settings.yakuza1_health == 0:
            self.yakuzas.remove(self.yakuza1)
                #self.sb.prep_score()
            #self.sb.check_highscore()
            #self.sb.prep_highscore()

    def _draw_floors(self):
        for floor in self.floors:
            floor.draw_platforms()

    def _draw_scoreboard(self):
        """Method to draw level and health"""
        self.sb.prep_health()
        self.sb.prep_level()
        self.sb.show_health()
        self.sb.show_level()

    def _update_screen(self):
        # redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_colour)
        self._draw_floors()
        self.hero.blitme()
        self._draw_fires()
        self._draw_yakuza()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self._update_bullets()
        self.door.blitme()
        self._draw_scoreboard()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ya = YakuzaAttack()
    ya.run_game()