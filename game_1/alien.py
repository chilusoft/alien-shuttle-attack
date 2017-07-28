import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''
    class for a single alien in the fleet
    '''

    def __init__(self,g_settings,scr):
        '''
        creates alien and sets its position
        :return:
        '''
        super(Alien,self).__init__()
        self.scr = scr
        self.g_settings = g_settings

        #loads alien and sets its rect attribute
        self.image = pygame.image.load('src/rsrcs/images/alien.png')
        self.rect = self.image.get_rect()

        #each new alien starts near the top left of the screem
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the aliens position as a float
        self.x = float(self.rect.x)

    def check_ends(self):
        '''
        :returns true if the alien fleet hit the edge
        :return:
        '''
        scr_rect = self.scr.get_rect()
        if self.rect.right >= scr_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        '''
        draw alien at current position
        :return:
        '''

        self.scr.blit(self.image,self.rect)

    def update(self,):
        '''
        move the alien right or left
        :return:
        '''

        self.x += (self.g_settings.alien_speed_factor * self.g_settings.fleet_direction)
        self.rect.x = self.x

