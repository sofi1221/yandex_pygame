import pygame
import os

def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    return image

