import pygame
import sys

def update_screen(screen):
    screen_color = (210,229,184)

    screen.fill(screen_color)

    pygame.display.flip()

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('w')
            if event.key == pygame.K_s:
                print('s')
            if event.key == pygame.K_a:
                print('a')
            if event.key == pygame.K_d:
                print('d')
            if event.key == pygame.K_q:
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                print('w')
            if event.key == pygame.K_s:
                print('s')
            if event.key == pygame.K_a:
                print('a')
            if event.key == pygame.K_d:
                print('d')

