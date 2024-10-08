class Settings:
    def __init__(self):
        # Display settings
        self.screen_width = 1100
        self.screen_height = 600
        
        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_speed_factor = 3
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 5
        
        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 8
        self.fleet_direction = 1  # 1 stands for right, -1 stands for left
        
        self.speedup_scale = 1.1
        self.score_scale = 2.5
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50
        
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
