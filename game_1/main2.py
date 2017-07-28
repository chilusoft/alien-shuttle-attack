import pygame
from pygame.sprite import  Group
import sys
from pygame.locals import *
from settings import Settings
from shuttle import Shuttle
import g_funct as gf
from alien import Alien



def start_game():
    pygame.init()
    g_settings = Settings()
    scr = pygame.display.set_mode((g_settings.scr_width,g_settings.scr_height))
    pygame.display.set_caption('Alien-Shuttle War 1')

    shuttle = Shuttle(g_settings,scr)
    alien = Alien(g_settings,scr)
    #make a group to store bullets
    bullets = Group()
    aliens = Group()

    #create the fleet of aliens.
    gf.create_fleet(g_settings,scr,shuttle,aliens)

    while True:
        gf.check_events(g_settings,scr,shuttle,bullets)
        shuttle.update()
        gf.refresh_bullets(g_settings,scr,shuttle,aliens,bullets)
        gf.refresh_aliens(g_settings,shuttle,aliens)
        gf.refresh_scr(g_settings,scr,shuttle,aliens,bullets)


start_game()