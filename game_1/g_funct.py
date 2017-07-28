__author__ = 'Chilufya'

import pygame,sys
from pygame.locals import *
from bullet import Bullet
from alien import Alien



def check_fleet_edges(g_settings,aliens):
    '''
    triggers a response if an alien hits the screen edge
    :param g_settings:
    :param aliens:
    :return:
    '''
    for alien in aliens.sprites():
        if alien.check_ends():
            change_fleet_direction(g_settings,aliens)
            break

def change_fleet_direction(g_settings,aliens):
    '''
    drops entire and changes direction
    :param g_settings:
    :param aliens:
    :return:
    '''
    for alien in aliens.sprites():
        alien.rect.y += g_settings.fleet_drop_speed
    g_settings.fleet_direction *= -1



def refresh_aliens(g_settings,shuttle,aliens):
    '''
    checks if an alien is at the edge and then
    updates positions of aliens
    :param aliens:
    :return:
    '''
    check_fleet_edges(g_settings,aliens)
    aliens.update()

    #look for alien ship collision
    if pygame.sprite.spritecollideany(shuttle,aliens):
        print 'shuttle hit!!'


def get_number_rows(g_settings,shuttle_height,alien_height):
    '''
    dtermine number of aliens that fit on the screen
    :param g_settings:
    :param shuttle_height:
    :param alien_height:
    :return:
    '''
    avail_space_y = (g_settings.scr_height - (3 * alien_height) - shuttle_height)
    number_rows = int(avail_space_y / (2 * alien_height))
    return number_rows

def get_alien_number_x(g_settings,alien_width):
    avail_space_x = g_settings.scr_width - 2 * alien_width
    number_aliens_x = int(avail_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(g_settings,scr,aliens,alien_number,row_number):
    '''
    creates an alien and places it in a row
    :param g_settings:
    :param scr:
    :param aliens:
    :param alien_number:
    :return:
    '''
    alien = Alien(g_settings,scr)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(g_settings,scr,shuttle,aliens):
    '''
    full fleet of aliens is created
    :param g_settings:
    :param scr:
    :param aliens:
    :return:
    '''
    #create an alien and determine the number of aliens in a row.
    #Spacing between each alien is equal to one alien width


    alien = Alien(g_settings,scr)
    number_aliens_x = get_alien_number_x(g_settings,alien.rect.width)
    number_rows = get_number_rows(g_settings,shuttle.rect.height,alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(g_settings,scr,aliens,alien_number,row_number)






def refresh_bullets(g_settings,scr,shuttle,aliens,bullets):
    '''
    refresh the position of bullets with each loop in the main game while loop
    :param bullets:
    :return:
    '''
    #Update the position of a bullet
    bullets.update()
     #deletes bullets after they disappear from the screeen to prevent the game from lagging
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collision(g_settings,scr,shuttle,aliens,bullets)


def check_bullet_alien_collision(g_settings,scr,shuttle,aliens,bullets):
    '''
    responds to bullet collision
    :param g_settings:
    :param scr:
    :param shuttle:
    :param aliens:
    :param bullets:
    :return:
    '''
    #check for bullets that hit any alien,if so delete bullet and alien
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) == 0:
        #destroy bullets and create new fleet
        bullets.empty()
        create_fleet(g_settings,scr,shuttle,aliens)

def check_keydown_events(event,g_settings,scr,shuttle,bullets):
     if event.key == pygame.K_RIGHT:
        #moves shuttle to the right
        shuttle.moving_right = True


     elif event.key == pygame.K_LEFT:
        #moves the shuttle to the left
        shuttle.moving_left = True

     elif event.key == pygame.K_SPACE:
        fire_bullet(g_settings,scr,shuttle,bullets)

     elif event.key == pygame.K_q:
         sys.exit()

def fire_bullet(g_settings,scr,shuttle,bullets):
    #creates new bullet and adds it to the bullets group
    if len(bullets) < g_settings.bullets_allowed:
        new_bullet = Bullet(g_settings,scr,shuttle)
        bullets.add(new_bullet)

def check_keyup_events(event,shuttle):


    if event.key == pygame.K_RIGHT:
        shuttle.moving_right = False
    elif event.key == pygame.K_LEFT:
        shuttle.moving_left = False

def check_events(g_settings,scr,shuttle,bullets):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,g_settings,scr,shuttle,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,shuttle)
def refresh_scr(g_settings,scr,shuttle,aliens,bullets):
    scr.fill(g_settings.bg_color)
    #redraw all bullets behind shuttle and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    shuttle.blitme()
    aliens.draw(scr)
    pygame.display.update()
