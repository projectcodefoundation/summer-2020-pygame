import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))

image = pygame.image.load("image.png")
image = pygame.transform.scale(image, (200, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    screen.blit(image, (50, 50))
    
    pygame.display.flip()
