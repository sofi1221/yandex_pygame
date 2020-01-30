import pygame
import os


with open('statistic.txt', 'rt') as f:
    r = f.read()
    arr = [float(x) for x in r.split()]
    time = arr[0]
    comp = arr[1]
    igr = arr[2]
    best_comp = arr[3]
    best_igr = arr[4]
    lenqth = arr[5]