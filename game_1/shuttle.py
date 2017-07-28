import pygame


class Shuttle(object):

    def __init__(self,g_settings,scr):

        '''calls the shuttle and sets its starting position '''

        self.scr = scr
        self.g_settings = g_settings
        #load the shuttle image and get its rect(coordinates)

        self.image = pygame.image.load('src/rsrcs/images/shuttle.png')
        self.rect = self.image.get_rect()
        self.scr_rect  = scr.get_rect()

        #start shuttle at the bottom center of the scr
        self.rect.centerx = self.scr_rect.centerx
        self.rect.bottom = self.scr_rect.bottom

        self.center = float(self.rect.centerx)
        #movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


        #shuttle speed


    def update(self):
        '''
        :return:updates the ship position based on the movement flag
        '''
        if self.moving_right and self.rect.right < self.scr_rect.right:
            self.center += self.g_settings.shuttle_speed_multiplier
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.g_settings.shuttle_speed_multiplier
            '''
        elif self.moving_up:
            self.rect.centery -= 1
        elif self.moving_down:
            self.rect.centery += 1
            '''

        self.rect.centerx = self.center


    def blitme(self):
        '''draw shuttle at current position '''

        self.scr.blit(self.image,self.rect)
