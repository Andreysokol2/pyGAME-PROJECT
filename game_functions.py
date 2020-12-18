import pygame
import sys

def update_screen(screen, player):
    screen_color = (210,229,184)

    screen.fill(screen_color)
    player.draw_player()
    pygame.display.flip()

def check_events(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.UP = True
            elif event.key == pygame.K_s:
                player.DOWN = True
            elif event.key == pygame.K_a:
                player.LEFT = True
            elif event.key == pygame.K_d:
                player.RIGHT = True
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.UP = False
            elif event.key == pygame.K_s:
                player.DOWN = False
            elif event.key == pygame.K_a:
                player.LEFT = False
            elif event.key == pygame.K_d:
                player.RIGHT = False


