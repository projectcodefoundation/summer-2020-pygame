import pygame
import random

colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "magenta": (255, 0, 255),
    "cyan": (0, 255, 255),
    "white": (255, 255, 255)
}

balls = []


def random_color():
    return colors[random.choice(list(colors))]


def rot_center(image, rect, angle):
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect


def main():

    # Init Pygame

    pygame.init()

    clock = pygame.time.Clock()

    size = (960, 720)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Apple Frenzy")

    # Get Player Image

    player = pygame.transform.scale(pygame.image.load("Bowl.png"), (150, 100))
    p_rect = player.get_rect()
    p_rect.move_ip(415, 580)

    # Get Apple Image

    red_apple = pygame.transform.scale(pygame.image.load("RedApple.png"), (96, 120))
    gold_apple = pygame.transform.scale(pygame.image.load("GoldenApple.png"), (96, 120))

    # Game Variables

    velocity = 0
    ticks = 87
    mode = 0
    t_apples = 0
    status = 0
    apples = []

    # Play Music

    #pygame.mixer.music.load("Background.wav")
    #pygame.mixer.music.play(-1)

    # Game Loop

    while status == 0:

        # INPUT PROCESSING

        # Process Events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Process Keys

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if velocity > -60:
                velocity -= 10
        if keys[pygame.K_RIGHT]:
            if velocity < 60:
                velocity += 10

        # Move Player

        p_rect.move_ip(velocity, 0)

        # Reduce Velocity

        velocity *= 0.92

        # ADD APPLES

        if ticks % 87 == 0:
            if t_apples == 4:
                mode = 1
            a_rect = red_apple.get_rect() if mode == 0 else gold_apple.get_rect()
            a_x = random.randint(0, 864)
            a_rect.move_ip(a_x, -120)
            apples.append([a_rect, 0])
            t_apples += 1

        # DRAWING

        # Fill Background

        screen.fill((255, 0, 0) if mode > 0 and ticks % 4 == 1 else (0, 0, 0))

        # Draw Apples

        for i in range(len(apples)):
            apple = apples[i]
            screen.blit(*rot_center(red_apple if mode == 0 else gold_apple, apple[0], apple[1]))
            apple[0].move_ip(0, 10 if mode == 0 else 40)
            apple[1] += 4 if mode == 0 else 16
            apple[1] %= 360
            if apple[0].colliderect(p_rect) != 0:
                del apples[i]
                i -= 1
                continue
            elif apple[0].y > 720:
                del apples[i]
                i -= 1
                status = -1

        # Draw Player

        screen.blit(player, p_rect)

        # Update Display

        pygame.display.flip()

        # Tick Clock
        clock.tick(27)
        ticks += 1

    if status == -1:
        screen.fill((0, 0, 0))

main()
