import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))

rectangles = []

for i in range(10):
    x = random.randint(0, 550)
    y = random.randint(0, 350)
    dx = random.randint(1, 10)
    dy = random.randint(1, 10)
    color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
    rectangles.append([x, y, dx, dy, color])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    for rect in rectangles:
        pygame.draw.rect(screen, rect[4], (rect[0], rect[1], 50, 50))
        
        rect[0] += rect[2]
        rect[1] += rect[3]

        if rect[0] <= 0 or rect[0] + 50 >= 600:
            rect[2] = -rect[2]
        if rect[1] <= 0 or rect[1] + 50 >= 400:
            rect[3] = -rect[3]
    
    pygame.display.flip()
