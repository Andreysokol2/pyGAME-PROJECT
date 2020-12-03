import pygame
import sys

def update_screen(screen):
    screen_color = (255, 0, 0)

    screen.fill(screen_color)

    pygame.display.flip()

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

