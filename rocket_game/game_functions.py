import pygame
import sys

def check_events(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = True
                #rocket.rect.centerx += 1
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = True
                #rocket.rect.centerx -= 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = False
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = False

def screen_update(game_settings, screen, rocket):
    screen.fill(game_settings.bg_color)
    rocket.blitme()
    pygame.display.flip()

