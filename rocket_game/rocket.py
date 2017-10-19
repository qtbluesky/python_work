import pygame

class Rocket():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/rocket-icon.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)