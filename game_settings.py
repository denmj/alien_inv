
class Settings:
    def __init__(self):

        # Alien settings
        self.alien_speed = 3
        self.drop_speed = 25
        # 1 - right -1 - left
        self.direction = 1

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # rocket settings
        self.rocket_speed_factor = 10
        self.rocket_width = 5
        self.rocket_height = 20
        self.rocket_color = 255, 215, 0
        self.rocket_qnty = 3

        # ship settings
        self.ship_lives = 3

    def set_background(self):
        pass

