class Settings:
    """A class for the settings of the game"""
    def __init__(self):
        """Initialize all attributes of settings"""
        # Screen settings
        self.screen_height = 700
        self.screen_width = 1200
        self.bg_colour = (135,133,255)

        # Platform 1 settings
        self.floor_colour = (0,0,0)
        self.floor_height = 12

        # Hero settings
        self.gravity = 100
        self.times = []
        self.super_jump_times = []
        for i in range(1, 13):
            self.times.append(0.2)

        for i in range(1,25):
            self.super_jump_times.append(0.1)
        self.half_times = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
        #self.distance = -65

        # Yakuza settings
        self.yakuza_speed = 1
        self.yakuza_distance = 300
        self.yakuza_left_distance = -150
        self.yakuza_points = 5

        # Bullet settings
        self.bullet_speed = 5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = (0,0,0)
        self.number_of_bullets = 10

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.hero_speed = 0.5
        self.jump_velocity = -1.2 * self.gravity