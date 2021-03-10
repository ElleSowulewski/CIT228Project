class GameStats:
    """Track statistics for Honey Catch."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.players_left = self.settings.player_limit
        self.score = 0