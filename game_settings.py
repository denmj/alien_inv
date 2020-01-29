
class Settings:
    def __init__(self):

        self.game_active = False
        # Alien settings
        self.drop_speed = 5
        # 1 - right -1 - left
        self.direction = 1

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # rocket settings
        self.rocket_width = 5
        self.rocket_height = 20
        self.rocket_color = 255, 215, 0
        self.rocket_qnty = 5

        # ship settings
        self.ship_lives = 3

        # leveling up
        self.speedup_scale = 1.3

        self.dynamic_leveling()

    def set_background(self):
        pass

    def dynamic_leveling(self):
        self.player_ship_speed_factor = 1.5
        self.rocket_speed_factor = 10
        self.alien_speed = 3
        self.score_points = 1

    def increase_speed(self):
        self.player_ship_speed_factor *= self.speedup_scale
        self.rocket_speed_factor *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        print("Player ship speed: ", self.player_ship_speed_factor)
        print("Rocket speed: ", self.player_ship_speed_factor)
        print("Alien's speed: ", self.player_ship_speed_factor)

