import pygame


class Target():
    """Класс, представляющий движущиюся мишень"""

    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen

        # Создание мишени у правого края верхней части экрана
        self.rect = pygame.Rect(0, 0, ai_settings.target_width,
                                ai_settings.target_height)
        self.rect.x = 1120
        self.rect.y = 0
        self.color = ai_settings.target_color

    def draw_target(self):
        """Вывод мишени на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def rect_target(self):
        self.rect.x = 1119
        self.rect.y = 0



