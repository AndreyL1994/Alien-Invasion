import pygame
from pygame.sprite import Group

import training_functions as tf
from button import Button
from game_stats import GameStats
from settings import Settings
from ship import Ship
from target import Target


def run_training_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Training Shooting.")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    target = Target(ai_settings, screen)
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, 'play')

    while True:
        tf.check_events(ai_settings, screen, stats, play_button, ship, bullets, target)
        tf.update_screen(ai_settings, screen, stats, ship, bullets, target,
                         play_button)
        if stats.game_active:
            ship.update()
            tf.update_bullets(ai_settings, bullets, target)
            tf.update_target(target, ai_settings)
            tf.update_screen(ai_settings, screen, stats, ship, bullets, target,
                             play_button)
            tf.miss(ai_settings, stats, target)


run_training_game()
