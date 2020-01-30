import pygame
import random

pygame.init()
size = width, height = 1100, 700
screen = pygame.display.set_mode(size)
pos = (400, 350 + 175)
pos_vrag = (400, 175)
pos_shaiba = (400, 350)
x = 0
v_x = 0
v_y = 0
n = 0

schet_igr = 0
schet_comp = 0
obsh_igr = 0
obsh_comp = 0

theme = 0
level = 0

screen.fill((87, 87, 87))


class Hokkey:  # аэрохокей
    pass


class Board:
    pass
    # создание поля


class Minesweeper(Board):  # сапер
    pass


# hokkey.draw()
pygame.display.flip()
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(25)
# print(time, comp, igr)
