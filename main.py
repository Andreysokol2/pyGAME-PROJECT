import pygame
import game_functions as gf

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('pygame_game')

while True:
    gf.update_screen(screen)
    gf.check_events()