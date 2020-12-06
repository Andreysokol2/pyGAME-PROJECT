import pygame

class Player():


    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()



        self.TOP = False
        self.DOWN = False
        self.RIGHT = False
        self.LEFT = False