import pygame
import random
import os
import pymorphy2

schet_igr = 0
schet_comp = 0
obsh_igr = 0
obsh_comp = 0
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

    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, color_pole, (
                    self.left + self.cell_size * i, self.top + self.cell_size * j,
                    self.cell_size, self.cell_size), 0)
                pygame.draw.rect(screen, (20, 200, 255), (
                    self.left + self.cell_size * i, self.top + self.cell_size * j,
                    self.cell_size, self.cell_size), 1)


class Minesweeper(Board):  # сапер
    pass

    def render(self):
        pass


class Minesweeper(Board):
    def __init__(self, x, y):
        pass

    def drawing(self):
        pass

    def open_cell(self, pos, q):
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
