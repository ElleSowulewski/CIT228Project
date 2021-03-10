from player import Player

class Settings:
    """A class to store all settings for Honey Catch."""
    def __init__(self):
        """Initialize the game's static settings."""
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (179, 230, 255)

        self.player_speed = 5
        self.player_limit = 3
        self.score_scale = 1.5
        self.player_speed = 1.7
        self.drop_speed = 1

        self.drop_points = 50