import pygame

from settings import Settings
from rocket import Rocket
import game_functions as gf

def run_game():
    pygame.init()
    #pygame.display.init()

    game_setting = Settings()
    screen = pygame.display.set_mode([game_setting.screen_width, game_setting.screen_height])
    pygame.display.set_caption(game_setting.window_caption)
    rocket = Rocket(screen)

    while True:
        gf.check_events(rocket)
        if rocket.moving_right == True:
           rocket.rect.centerx += 1
        if rocket.moving_left == True:
           rocket.rect.centerx -= 1

        screen.fill(game_setting.bg_color)
        rocket.blitme()
        pygame.display.flip()
            
run_game()

