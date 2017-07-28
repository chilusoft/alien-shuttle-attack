__author__ = 'Chilufya'

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    ''' a class to play around with the bullets fired by the space shuttle
    '''
    def __init__(self,g_settings,scr,shuttle):
        '''
        creates a bullet object at the position of the ship
        :param g_settings:
        :param scr:
        :param shuttle:
        :return:
        '''
        super(Bullet,self).__init__()
        self.scr = scr
        #creates the bullet at origin and sets it to the correct position

        self.rect = pygame.Rect(0,0,g_settings.bullet_width,g_settings.bullet_height)
        self.rect.centerx = shuttle.rect.centerx
        self.rect.top = shuttle.rect.top


        #store the bullets position as a float
        self.y = float(self.rect.y)
        self.color = g_settings.bullet_color
        self.speed_factor = g_settings.bullet_speed_factor


    def update(self):
        '''
        moves the bullet up the screen
        :return:
        '''
        #refreshes the float position of the bullet
        self.y -= self.speed_factor
        #updates the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        '''
        draws bullet on the screen
        :return:
        '''

        pygame.draw.rect(self.scr, self.color,self.rect)
