import pygame

from pygame.sprite import Group

import game_functions as gf

from game_stats import GameStats

from scoreboard import Scoreboard

from button import Button

from settings import Settings

from ship import Ship


def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play")
    # Сохдание корабля
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль
    bullets = Group()
    # Создание группы пришельцев
    aliens = Group()
    # Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Создание экземпляров для хранения игровой статистики и очков.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)


    # Запуск основного цикла игры
    while True:
        # отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                             play_button)
            # При каждом проходе цикла перерисовывается экран
            screen.fill(ai_settings.bg_color)
            ship.blitme()
        else:
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                             play_button)
            gf.check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


run_game()
