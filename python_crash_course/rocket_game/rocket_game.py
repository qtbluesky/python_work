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
    rocket = Rocket(screen, game_setting)

    while True:
        gf.check_events(rocket)
        rocket.update()
        gf.screen_update(game_setting, screen, rocket)
'''
        screen.fill(game_setting.bg_color)
        rocket.blitme()
        pygame.display.flip()
'''

run_game()

