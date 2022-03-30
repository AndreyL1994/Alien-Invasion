import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, stats, screen, ship, target, bullets):
    """Проверяет нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        ai_settings.initialize_dynamic_settings()
        play_game(ai_settings, stats, ship, target, bullets)


def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, play_button, ship, bullets, target):
    """Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, stats, screen, ship, target, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, stats, play_button,
                              ship, bullets, target, mouse_x, mouse_y)


def check_play_button(ai_settings, stats, play_button, ship,
                      bullets, target, mouse_x, mouse_y):
    """Запускает игру при нажатии кнопки Play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        play_game(ai_settings, stats, ship, target, bullets)


def play_game(ai_settings, stats, ship, target, bullets):
    ai_settings.target_limit = 10
    pygame.mouse.set_visible(False)
    stats.game_active = True
    bullets.empty()
    target.rect_target()
    ship.center_ship()


def update_screen(ai_settings, screen, stats, ship, bullets, target,
                  play_button):
    """обновляет изображения на экране и прорисовывает новый экран"""
    # Прорисовывается новый экран при каждом переходе цикла
    screen.fill(ai_settings.bg_color)
    # Все пули выводятся позади корабля
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    target.draw_target()
    if not stats.game_active:
        play_button.draw_button()
    # Отображение последнего прорисованного экрана
    pygame.display.flip()


def update_bullets(ai_settings, bullets, target):
    """Обновляет позиции пуль и уничтожает старые пули."""
    # Обновлении позиций пуль
    bullets.update()
    # Уничтожение изчезнувших пуль
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            ai_settings.target_limit -= 1
    # Проверка попаданий в мишень.
        if pygame.sprite.spritecollideany(target, bullets):
            bullets.remove(bullet)
            ai_settings.shoots += 1
            ai_settings.increase_speed()


def update_target(target, ai_settings):
    """Двигает мишень в лево и в право."""
    target.rect.x -= ai_settings.target_speed_factor
    if target.rect.x <= 0:
        ai_settings.target_speed_factor *= -1
    if target.rect.x >= 1160:
        ai_settings.target_speed_factor *= -1


def miss(ai_settings, stats, target):
    """Обрабатывает промахи"""
    if ai_settings.target_limit <= 0:
        print('Quantity of hits is ' + str(ai_settings.shoots))
        ai_settings.shoots = 0
        stats.game_active = False
        pygame.mouse.set_visible(True)
        target.rect_target()









