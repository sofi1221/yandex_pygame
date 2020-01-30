import pygame
import random
import os
import pymorphy2


class Hockey:
    def draw(self):
        pass

    def otbit(self):
        pass

    def kraya(self):
        pass

    def vorota(self):
        pass

    def vozvrat(self):
        pass


class Board:
    # создание поля
    def __init__(self, width, height):
        pass

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
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
        all_sprites.update(event)
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(25)
# print(time, comp, igr)
