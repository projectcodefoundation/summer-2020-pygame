import pygame
import random
import time
import sys

pygame.init()

screen = pygame.display.set_mode((430, 430))

# loading the images into the dictionary

image_names = ["kaede", "komachi", "kei",
               "kaori", "karen", "kirino", "kumiko", "kotori"]

images = {}
for name in image_names:
    images[name] = pygame.image.load(name + ".jpg")
    images[name] = pygame.transform.scale(images[name], (100, 100))

# 2d list of where each image is

board = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
]

all_images = image_names * 2

for i in range(4):
    for j in range(4):
        name = random.choice(all_images)
        board[i][j] = images[name]
        all_images.remove(name)

# 0: hidden, 1: revealed
state = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            click_i = x // 110
            click_j = y // 110
            state[click_i][click_j] = 1

    screen.fill((0, 0, 0))

    # loop through each row and column
    for i in range(4):
        for j in range(4):
            if state[i][j] == 0:
                pygame.draw.rect(screen, (255, 0, 0),
                                 (i * 110, j * 110, 100, 100))
            else:
                image = board[i][j]
                screen.blit(image, (i * 110, j * 110))

    pygame.display.flip()
