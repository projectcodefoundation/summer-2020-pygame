import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((400, 600))

player = pygame.Rect(175, 550, 50, 20)
rects = []

def make_rect():
    x = random.randint(0, 350)
    color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
    return [x, -100, color]

frame = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # logic

    if frame % 20 == 0:
        rects.append(make_rect())

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.move_ip(-10, 0)
    if keys[pygame.K_RIGHT]:
        player.move_ip(10, 0)

    # drawing
            
    screen.fill((0, 0, 0))

    for idx, rect in enumerate(rects):
        pygame.draw.rect(screen, rect[2], (rect[0], rect[1], 50, 50))

        if player.colliderect((rect[0], rect[1], 50, 50)):
            sys.exit()

        rect[1] += 5

        if rect[1] > 600:
            rects[idx] = None

    rects = [x for x in rects if x is not None]

    pygame.draw.rect(screen, (255, 255, 255), player)

    pygame.display.flip()

    frame += 1
