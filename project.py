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
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

# настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size




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
