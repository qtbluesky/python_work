import pygame
import sys

class Rocket():
    def __init__(self, screen, game_setting):
        self.screen = screen
        self.game_setting = game_setting
        self.image = pygame.image.load('rocket-icon.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False





    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.speed
        if self.moving_left == True and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.speed