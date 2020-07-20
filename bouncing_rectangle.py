import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))

x = 0
y = 0

dx = 4
dy = 4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50)) 
    pygame.display.flip()

    x += dx
    y += dy

    if x <= 0 or x + 50 >= 600:
        dx = -dx
    if y <= 0 or y + 50 >= 400:
        dy = -dy
