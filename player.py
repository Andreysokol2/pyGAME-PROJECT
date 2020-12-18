import pygame

class Player():


    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.player_image = pygame.image.load('images/player.gif')
        self.player_rect = self.player_image.get_rect()
        self.player_rect.left = self.screen_rect.left
        self.player_rect.bottom = self.screen_rect.bottom

        self.UP = False
        self.DOWN = False
        self.RIGHT = False
        self.LEFT = False

        self.speed = 1

    def draw_player(self):
        self.screen.blit(self.player_image, self.player_rect)

    def update(self):
        if self.UP:
            self.player_rect.y -= self.speed
        elif self.DOWN:
            self.player_rect.y += self.speed
        elif self.LEFT:
            self.player_rect.x -= self.speed
        elif self.RIGHT:
            self.player_rect.x += self.speed