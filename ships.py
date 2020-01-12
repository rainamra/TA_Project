import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        # intialize ship and set starting position
        super(Ship, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store decmial value for ships center
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # draw ship at current location
        self.screen.blit(self.image, self.rect)

    def update(self):
        # update ships position based on movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update object from self.center
        self.rect.centerx = self.center

    def center_ship(self):
        # center ship on screen
        self.center = self.screen_rect.centerx