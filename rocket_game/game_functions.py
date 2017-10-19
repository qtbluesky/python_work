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

