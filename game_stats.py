class GameStats:
    """Track statistics for Alien Invasion"""
    def __init__(self, ya_game):
        self.settings = ya_game.settings
        self.reset_stats()
        # Start Yakuza Attack in an inactive state.
        self.game_active = True
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.health = 100.0
        self.points = 0
        self.level = 1
        """with open('highscore.txt') as file_object:
           highscoretry = file_object.read()
           self.highscore = float(highscoretry)"""
