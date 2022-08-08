class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize Game's Settings."""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 760
        self.bg_color = (0, 0, 230)

        #ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 1

        #creating settings for fleet direction
        self.fleet_drop_speed = 10
        #fleet direction of 1 rep right; -1 rep left
        self.fleet_direction = 1

        

