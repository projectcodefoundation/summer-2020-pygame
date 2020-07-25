import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((400, 600))

blocks = []
px = 175
counter = 0
lives = 3

block_speed = 3
block_frequency = 40

font = pygame.font.SysFont(None, 35)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Listen for keyboard input and move player

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        px = min(px + 5, 350)
    if keys[pygame.K_LEFT]:
        px = max(px - 5, 0)

    # New block every 20 frames
    if counter % block_frequency == 0:
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        
        if random.randint(1, 15) == 1:
            block_type = "life"
        else:
            block_type = "block"
            
        while color == (0, 0, 0):
            color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
        blocks.append([
            random.randint(0, 350),
            -50,
            color,
            block_type
        ])

    if counter == 400:
        block_speed = 5
        block_frequency = 20
    if counter == 1000:
        block_speed = 8
        block_frequency = 15

    screen.fill((0, 0, 0))

    # Blocks

    player_rect = pygame.Rect(px, 550, 50, 20)

    new_blocks = []
    for block in blocks:
        if block[3] == "block":
            pygame.draw.rect(screen, block[2], (block[0], block[1], 50, 50))
        elif block[3] == "life":
            pygame.draw.ellipse(screen, block[2], (block[0], block[1], 50, 50))

        # check if the player is overlapping with the block
        if player_rect.colliderect((block[0], block[1], 50, 50)):
            if block[3] == "block":
                lives -= 1
                if lives == 0:
                    pygame.quit()
                    sys.exit()
            elif block[3] == "life":
                lives += 1
        else:
            # move the block down
            block[1] += block_speed

            if block[1] < 600:
                new_blocks.append(block)
            
    blocks = new_blocks

    # Player
    pygame.draw.rect(screen, (255, 255, 255), (px, 550, 50, 20))

    # Lives
    img = font.render("Lives: " + str(lives), True, (255, 255, 255))
    screen.blit(img, (20, 20))

    # Update
    pygame.display.flip()
    pygame.time.wait(10)
    counter += 1
    
