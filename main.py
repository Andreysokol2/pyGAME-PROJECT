import pygame
import game_functions as gf
from player import Player

pygame.init()

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('pygame_game')

player = Player(screen)

while True:
    gf.update_screen(screen)
    gf.check_events()