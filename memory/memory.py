import pygame
import random
import time
import sys

pygame.init()

screen = pygame.display.set_mode((430, 430))

image_names = ["kaede", "kaguya", "kanna", "kaori", "karen", "kirino", "kumiko", "kyoko"]

images = {}

for name in image_names:
    images[name] = pygame.transform.smoothscale(pygame.image.load(name + ".jpg"), (100, 100))

board = [
    [images["karen"], images["kyoko"], images["kanna"], images["kaori"]], 
    [images["kaguya"], images["kanna"], images["kirino"], images["kyoko"]], 
    [images["kaori"], images["kirino"], images["kumiko"], images["kaguya"]], 
    [images["kumiko"], images["karen"], images["kaede"], images["kaede"]],
]

stage = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

pi = None
pj = None
ni = None
nj = None

pframe = -1
frame = 0

while True:
    # check events
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            sys.exit()
        
        # click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # get clicked tile
            x, y = event.pos
            i, j = x // 110, y // 110

            # if not revealed yet
            if stage[i][j] == 0:

                # first one clicked
                if pi == None:
                    pi, pj = i, j
                    stage[i][j] = 1

                # second one clicked
                elif ni == None:
                    # if matches
                    if board[i][j] == board[pi][pj]:
                        stage[pi][pj] = 2
                        stage[i][j] = 2
                        pi = None
                        pj = None
                    else:
                        stage[pi][pj] = 1
                        stage[i][j] = 1

                        ni, nj = i, j
                        pframe = frame + 30
            
    if frame == pframe:
        stage[pi][pj] = 0
        stage[ni][nj] = 0
        pi = None
        pj = None
        ni = None
        nj = None

    screen.fill((0, 0, 0))

    for i in range(4):
        for j in range(4):
            if stage[i][j] == 0:
                pygame.draw.rect(screen, (255, 0, 0), (i * 110, j * 110, 100, 100))
            else:
                screen.blit(board[i][j], (i * 110, j * 110))

    pygame.display.flip()
    frame += 1

