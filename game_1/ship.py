import pygame


class Shuttle(object):

    def __init__(self,scr):

        '''calls the shuttle and sets its starting position '''

        self.scr = scr

        #load the shuttle image and get its rect(coordinates)

        self.image = pygame.image.load('src/rsrcs/images/shuttle.png')
        self.rect = self.image.get_rect()
        self.scr_rect  = scr.get_rect()

        #start shuttle at the bottom center of the scr
        self.rect.centerx = self.scr_rect.centerx
        self.rect.bottom = self.scr_rect.bottom

    def blitme(self):
        '''draw shuttle at current position '''

        self.scr.blit(self.image,self.rect)
