class Settings(object):

    ''' class that store all the settings '''

    def __init__(self):
        ''' calls the game settings '''
        self.scr_width = 1200
        self.scr_height = 640
        self.bg_color = (0,0,0)
        #shuttle speed
        self.shuttle_speed_multiplier = 1.5

        #bullets
        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 47, 80
        self.bullets_allowed = 3

        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet direction of 1 represnts right; -1 means left
        self.fleet_direction = 1


        
