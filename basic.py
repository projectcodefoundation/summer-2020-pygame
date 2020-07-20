import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 300)) 
    pygame.display.flip()
