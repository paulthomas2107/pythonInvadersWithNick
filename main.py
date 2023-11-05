import pygame
import sys
import random
from game import Game

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50

GREY = (29, 29, 27)
YELLOW = (243, 216, 63)

screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + (2 * OFFSET)))
pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERY_SHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERY_SHIP, random.randint(4000, 8000))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot_laser()
        if event.type == MYSTERY_SHIP and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERY_SHIP, random.randint(4000, 8000))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run is False:
            game.reset()

    # Updating
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.check_for_collisions()

    # Drawing
    screen.fill(GREY)
    pygame.draw.rect(screen,
                     YELLOW,
                     (10, 10, 780, 780),
                     2,
                     0,
                     60,
                     60,
                     60,
                     60)
    pygame.draw.line(screen,
                     YELLOW,
                     (25, 730), (775, 730), 3)
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)

    pygame.display.update()
    clock.tick(60)