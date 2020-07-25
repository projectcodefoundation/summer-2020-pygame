import pygame
import random
import time
import sys

pygame.init()

screen = pygame.display.set_mode((430, 430))

image_names = ["kaede", "komachi", "kei",
               "kaori", "karen", "kirino", "kumiko", "kotori"]

images = {}

for name in image_names:
    images[name] = pygame.transform.smoothscale(
        pygame.image.load(name + ".jpg"), (100, 100)
    )

board = [
    [images["karen"], images["kotori"], images["kei"], images["kaori"]],
    [images["komachi"], images["kei"], images["kirino"], images["kotori"]],
    [images["kaori"], images["kirino"], images["kumiko"], images["komachi"]],
    [images["kumiko"], images["karen"], images["kaede"], images["kaede"]],
]

state = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

prev_i, prev_j = None, None

while True:
    wait = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # get clicked tile
            x, y = event.pos
            click_i, click_j = x // 110, y // 110

            if state[click_i][click_j] == 0:

                # first image clicked
                if prev_i == None:
                    prev_i, prev_j = click_i, click_j
                    state[click_i][click_j] = 1

                # second image clicked
                else:
                    if board[click_i][click_j] == board[prev_i][prev_j]:
                        state[click_i][click_j] = 2
                        state[prev_i][prev_j] = 2
                        prev_i, prev_j = None, None
                    else:
                        state[click_i][click_j] = 1
                        wait = True

    screen.fill((0, 0, 0))

    for i in range(4):
        for j in range(4):
            if state[i][j] == 0:
                pygame.draw.rect(screen, (255, 0, 0),
                                 (i * 110, j * 110, 100, 100))
            else:
                screen.blit(board[i][j], (i * 110, j * 110))

    pygame.display.flip()

    if wait:
        pygame.time.wait(500)
        state[click_i][click_j] = 0
        state[prev_i][prev_j] = 0
        prev_i, prev_j = None, None

