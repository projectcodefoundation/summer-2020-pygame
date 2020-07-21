import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, (255, 0, 0), event.pos, 30)

    pygame.display.flip()
