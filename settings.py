class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # параметры пули
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Настройка пришельцев
        self.fleet_drop_speed = 10

        # Парвметры учебной мишени
        self.target_speed_factor = 1
        self.target_width = 80
        self.target_height = 10
        self.target_color = 100, 150, 100
        self.shoots = 0
        self.target_limit = 10

        # Темп ускорения игры
        self.speedup_scale = 1.3

        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.target_speed_factor = 1
        self.alien_points = 50

        # fleet_direction = 1 обозначает движение вправо; a -1 влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.target_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


