import pygame
import sys
import os
from settings import Settings
from shuttle import Shuttle


''' game window and infinte loop'''

def run_game():
    #initialise the game window

    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("Alien Attack 1")

    #makes a shuttle object
    shuttle = Shuttle(screen)
    


    #start the loop for the game

    while True:
        #detect keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #refresh screen after color change
        screen.fill(game_settings.bg_color)
        shuttle.blitme()

        #refreshes the game screen
        pygame.display.flip()


run_game()

