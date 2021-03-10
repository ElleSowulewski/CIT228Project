import pygame
import sys
import random
from settings import Settings
from player import Player
from drop import Drop
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class HoneyCatch:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Honey Catch")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.player = Player(self)
        self.drops = pygame.sprite.Group()

        self.play_button = Button(self, "Play")
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.player.update()
                if len(self.drops.sprites()) <=0:
                    self._create_drop() 
                           
            self._update_drops()
            self._update_screen()
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_q:
            running=False
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False

    def _update_drops(self):
        """Update the positions of all drops."""
        for drop in self.drops.sprites():
            self.drops.update()
            self._check_drops_bottom()

        if pygame.sprite.spritecollideany(self.player, self.drops):
            self._player_hit()
    
    def _create_drop(self):
        """Create an drop and place it."""
        drop = Drop(self)
        self.drops.add(drop)   

    def _check_drops_bottom(self):
        """Check if any drops have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for drop in self.drops.sprites():
            if drop.rect.bottom >= screen_rect.bottom:
                self.drops.empty()
                if self.stats.players_left > 0:
                    self.stats.players_left -= 1
                    self.sb.prep_players() 
                    self.drops.empty()

                else:
                    self.stats.game_active = False
                    pygame.mouse.set_visible(True)
   
    def _player_hit(self):
        """If player was hit by a drop"""
        self.stats.score += self.settings.drop_points
        self.drops.empty()
        self.sb.prep_score()
        self.sb.check_high_score()

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_players()

            self.drops.empty()
            self.player.center_player()

            pygame.mouse.set_visible(False)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        self.drops.draw(self.screen)

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    ai = HoneyCatch()
    ai.run_game()